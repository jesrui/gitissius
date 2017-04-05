import gitissius.commands as commands
import gitissius.gitshelve as gitshelve

class Command(commands.GitissiusCommand):
    """
    Push issues to remote
    """
    name = "push"
    aliases = []
    help = "Push issues upstream"

    def __init__(self):
        super(Command, self).__init__()

        self.parser.set_usage("%prog push")

    def _execute(self, options, args):
        # TODO use git config branch.gitissius.remote instead of hardcoded origin
        gitshelve.git('push', 'origin', 'gitissius')
