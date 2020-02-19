import sys
from argparse import ArgumentParser
import numpy as np
# import lif_meanfield_tools as lmt
import lif_meanfield_tools_zajzi as lmt

ureg = lmt.ureg


def create_parser():
    """
    Create command line parser with options.

    :return: ArgumentParser
    """
    parser_ = ArgumentParser(prog="calculate_fr.py")
    parser_.add_argument("--params", dest="params", nargs='*', default=[], metavar="extra arguments",
                         help="extra arguments for the computation function")
    return parser_


args = create_parser().parse_args(sys.argv[1:])  # avoids PyNEST sys.argv pollution
parameters = dict([arg.split('=', 1) for arg in args.params])
print(parameters)


# # instantiate network
network = lmt.Network(network_params='minimal_negative_M3.yaml',
                      analysis_params='analysis_params.yaml',
                      new_network_params={
                          # 'g': np.float(parameters['gamma']),
                          # 'nu_ext': np.float(parameters['nuX']) * ureg.Hz,
                          # 'w': np.float(parameters['w']) * ureg.pA,
                          # 'N': [20000, 100]
                      })

# calculate working point
working_point = network.working_point()

# print results
print('Working point:')
print('mean input: {}'.format(working_point['mean_input']))
print('std input: {}'.format(working_point['std_input']))
print('firing rates: {}'.format(working_point['firing_rates']))
print(working_point['firing_rates'])
print([x.item() for x in working_point['firing_rates']])




# # Minimal working example
#
# import lif_meanfield_tools as lmt
# ureg = lmt.ureg
#
# # instantiate network
# network = lmt.Network(network_params='network_params_microcircuit.yaml',
#                       analysis_params='analysis_params.yaml',
#                       new_network_params={})
#
# # calculate working point
# working_point = network.working_point()
#
# # print results
# print('Working point:')
# print('mean input: {}'.format(working_point['mean_input']))
# print('std input: {}'.format(working_point['std_input']))
# print('firing rates: {}'.format(working_point['firing_rates']))
#
# # print(network.transfer_function())
# print(network.transfer_function(10*ureg.Hz))
#
# # save results
# network.save()
