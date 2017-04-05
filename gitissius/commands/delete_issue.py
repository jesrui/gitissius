import gitissius.commands as commands
import gitissius.gitshelve as gitshelve
import gitissius.common as common

class Command(commands.GitissiusCommand):
    """ Delete an issue """
    name = "delete"
    aliases = ["d"]
    help = "Delete an issue"

    def __init__(self):
        super(Command, self).__init__()

        self.parser.set_usage("%prog delete issue_id")

    def _execute(self, option, args):
        # find issue
        try:
            issue_id = args[0]

        except IndexError:
            self.parser.print_usage()
            return

        issue = common.issue_manager.get(issue_id)

        if not common.verify("Delete issue '%s' (y)? " % issue.get_property('title'), default='y'):
            print " >", "Delete canceled"
            return

        issue.delete()

        # commit
        common.git_repo.commit("Deleted issue %s" % issue.get_property('id'))

        print "Deleted issue: %s" % issue.get_property('id')



