import gitissius.commands as commands
import gitissius.common as common

class Command(commands.GitissiusCommand):
    """
    List Issues
    """
    name="list"
    aliases = ['l']
    help="List issues"

    def __init__(self):
        super(Command, self).__init__()

        self.parser.add_option("--sort",
                               metavar='KEY',
                               help="Sort results using KEY")
        self.parser.add_option("--filter",
                               default=None,
                               metavar='KEY:VAL',
                               help="show only issues where KEY matches VAL (e.g. type:bug)")
        self.parser.add_option("--all",
                               default=False,
                               action="store_true",
                               help="List all issues, " \
                               "including closed and invalid"
                               )

    def _execute(self, options, args):
        if options.all:
            filters = []

        else:
            # default filters, to filter out invalid and closed issues
            filters = [{'status__not':'closed'}, {'status__not':'invalid'}]

        if options.filter:
            for fltr in options.filter.split(","):
                try:
                    key, value = fltr.split(':')

                except ValueError:
                    # filter parameters in worng format
                    print "Wrong filter argument:", fltr
                    return

                filters.append({key:value})

        common.print_issues(common.issue_manager.filter(sort_key=options.sort,
                                                        rules=filters)
                            )
