import gitissius.commands as commands
import gitissius.common as common

class Command(commands.GitissiusCommand):
    """ Edit an issue """

    name="edit"
    aliases = ['e']
    help="Edit an issue"

    def __init__(self):
        super(Command, self).__init__()

        self.parser.set_usage("%prog edit issue_id")

    def _execute(self, options, args):
        # find issue
        try:
            issue_id = args[0]

        except IndexError:
            self.parser.print_usage()
            return

        issue = common.issue_manager.get(issue_id)

        # edit
        issue.interactive_edit()

        if not common.verify("Save changes (y)? ", default='y'):
            print " >", "Issue discarded"
            return

        # add to repo
        common.git_repo[issue.path] = issue.serialize(indent=4)

        # commit
        common.git_repo.commit("Edited issue %s" % issue.get_property('id'))

        print "Edited issue: %s" % issue.get_property('id')
