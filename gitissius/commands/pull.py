import gitissius.commands as commands
import gitissius.gitshelve as gitshelve
import gitissius.common as common

class Command(commands.GitissiusCommand):
    """
    Pull issues to repo
    """
    name="pull"
    help="Pull issues from upstream"

    def _execute(self, options, args):
        # save current branch name
        branch = gitshelve.git('name-rev', '--name-only', 'HEAD') or 'master'

        # stash changes
        try:
            gitshelve.git('stash')

        except gitshelve.GitError, error:
            if 'You do not have the initial commit yet' in error.stderr:
                # don't worry, we just created 'gitissius' branch
                pass

            else:
                raise

        else:
            # switch branches
            gitshelve.git('checkout', 'gitissius')

        # pull updates
        gitshelve.git('pull')

        # switch back to previous branch
        gitshelve.git('checkout', branch)

        # pop stashed changes
        try:
            gitshelve.git('stash', 'pop')

        except gitshelve.GitError, error:
            # no worries, no stash to apply
            pass

        # XXX if the pull produced a merge commit we must re-init gitshelve
        # so that it sees commits from all merge parents.
        common.git_repo = gitshelve.open(branch='gitissius')

        # build issue list cache
        common.issue_manager.update_db()

