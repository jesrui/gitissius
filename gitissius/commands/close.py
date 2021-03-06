import gitissius.commands as commands
import gitissius.common as common

class Command(commands.GitissiusCommand):
    """
    Close Issue
    """
    name = "close"
    aliases = []
    help="Close an issue"

    def __init__(self):
        super(Command, self).__init__()

        self.parser.set_usage("%prog close issue_id")

    def _execute(self, options, args):
        # find issue
        try:
            issue_id = args[0]

        except IndexError:
            self.parser.print_usage()
            return

        issue = common.issue_manager.get(issue_id)

        # close issue
        if issue.get_property('status').value == 'closed':
            print " >", "Issue already closed"
            return

        issue.get_property('status').value = 'closed'
        issue.get_property('updated_on').value = common.now()

        # add to repo
        common.git_repo[issue.path] = issue.serialize(indent=4)

        # commit
        common.git_repo.commit("Closed issue %s" % issue.get_property('id'))

        print "Closed issue: %s" % issue.get_property('id')
