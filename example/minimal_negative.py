import os
import sys
import numpy as np
import itertools
# import lif_meanfield_tools as lmt  # instead we use the modified version below..

# path to manual LIF tool
dir_prefix = './'
np.set_printoptions(threshold=sys.maxsize)

sys.path.append('/home/zbarni/code/projects/lif_meanfield_tools/')
import lif_meanfield_tools_zajzi as lmt

def solve_mft_rates(parameters_):
    network_ = lmt.Network(
        network_params=os.path.join(dir_prefix, 'minimal_negative_M3.yaml'),
        analysis_params=os.path.join(dir_prefix, 'analysis_params.yaml'),
        new_network_params=parameters_,
    )

    network_.network_params['W'] = parameters_['W']
    working_point = network_.working_point()

    return network_, working_point['firing_rates']


if __name__ == "__main__":

    parameters = {
        # need to create the weight matrix manually:
        # - wE=32.28, wI=-g*wE, with g=12
        # - populations are defined recursively in groups of 4 as E, E, I, I..
        'W': np.array([list(itertools.chain(*([32.28,   32.28, -387.36, -387.36] for _ in range(3)))) \
                       for _ in range(12)]) * lmt.ureg.pA,
        'w': 32.28 * lmt.ureg.pA
    }
    network, result = solve_mft_rates(parameters)

    for pop_idx, pop in enumerate(network.network_params['populations']):
        print('\t{0} @ {1:.2f}'.format(pop, result[pop_idx]))
