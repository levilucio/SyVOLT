
import argparse

def load_parser():
    parser = argparse.ArgumentParser(description='Run the test.')

    parser.add_argument('--skip_tests', dest = 'run_tests', default = True, action = 'store_false',
                        help = 'Option to skip the running of matching tests')

    parser.add_argument('--skip_progress_bar', dest = 'show_progress_bar', default = True, action = 'store_false',
                        help = 'Option to skip the showing of a progress bar')

    parser.add_argument('--skip_parallel', dest = 'do_parallel', action = 'store_false',
                        help = 'Option to force computation to run single-thread')
    parser.set_defaults(do_parallel = True)

    parser.add_argument('--skip_pickle', dest = 'do_pickle', action = 'store_false',
                        help = 'Option to skip the use of pickling')
    parser.set_defaults(do_pickle = True)

    parser.add_argument('--compression', type = int, default = 6,
                        help = 'Level of compression to use with pickling. Range: 0 (no compression) to 9 (high compression) (default: 6)')
    parser.set_defaults(compression = 6)

    parser.add_argument('--slice', type = int, default = -1,
                        help = 'Index of contract to slice for. Range: -1 (no slicing) to #CONTRACTS-1 (default: -1)')
    parser.set_defaults(slice = -1)

    parser.add_argument('--draw_svg', dest = 'draw_svg', action = 'store_true', default = False,
                        help = 'Flag to force svg files to be drawn (default: False)')

    parser.add_argument('--draw_rules', dest = 'draw_rules', action = 'store_true', default = False,
                        help = 'Flag to force rule svg files to be drawn (default: False)')
    
    parser.add_argument('--num_pcs', type = int, default = -1,
                        help = 'Number of path conditions which should be produced by this test (default: -1)')

    parser.add_argument('--num_rules', type = int, default = -1,
                        help = 'Number of rules in the transformation (default: -1)')

    parser.add_argument('--verbosity', type = int, default = 0,
                        help = 'Verbosity level (default: 0 - minimum output)')

    parser.add_argument('--contract', type = int, default = -1,
                        help = 'Contract selection (default: -1 - no contract)')
    parser.set_defaults(contract = -1)

    parser.add_argument('--handbuilt', dest = 'handbuilt', action = 'store_true',
                        help = 'Select the handbuilt version (default: False - use HOT version)')
    parser.set_defaults(handbuilt = False)

    parser.add_argument('--load', dest = 'pc_filename', nargs='?', const="", type=str,
                        help = 'Input the txt filename that contains the PC filenames you want to load')

    return parser

