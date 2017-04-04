import gitissius.commands as commands
import gitissius.gitshelve as gitshelve

class Command(commands.GitissiusCommand):
    """
    Push issues to repo
    """
    name = "push"
    aliases = []
    help = "Push issues upstream"

    def _execute(self, options, args):
        # TODO use git config branch.gitissius.remote instead of hardcoded origin
        gitshelve.git('push', 'origin', 'gitissius')
