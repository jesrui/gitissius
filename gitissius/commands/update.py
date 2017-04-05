import gitissius.commands as commands
import gitissius.gitshelve as gitshelve

class Command(commands.GitissiusCommand):
    """
    Pull issues from remote, then push
    """
    name="update"
    aliases = ['u']
    help="Pull issues from upstream and then push"

    def __init__(self):
        super(Command, self).__init__()

        self.parser.set_usage("%prog update")

    def _execute(self, options, args):
        from pull import Command as pull
        from push import Command as push

        # this looks funny, because we first create a Command object
        # and then we execute it
        pull()(None)
        push()(None)

