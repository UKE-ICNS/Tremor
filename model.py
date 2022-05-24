#This will be a file for a PD tremor project
import matplotlib
from netpyne import specs, sim 
from neuron import h
import os

%matplotlib auto

os.chdir(r"C:\Users\Mariia Popova\Desktop\PhD\Code\Tremor model\Tremor")

!nrnivmodl

#%% Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

#%% Create cells

# Initialize ion concentrations for stn and gpe/i neurons
h("cai0_ca_ion = 5e-6 ")
h("cao0_ca_ion = 2")
h("ki0_k_ion = 105") 
h("ko0_k_ion = 3")
h("nao0_na_ion = 108")
h("nai0_na_ion = 10")

# from hahn, fleming, nambu, otsuka
netParams.cellParams['GPe'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 60,
                "L": 60,
                "Ra": 200.0,
                "cm": 1
            },
            "mechs": {
                'myions': {},
                "GPeA": {
                    "gnabar": 0.04,
                    "gkdrbar": 0.0042,
                    "gkcabar": 0.1e-3, 
                    "gcatbar": 6.7e-5, 
                    "kca": 2, 
                    "gl": 4e-5
                }
            }
        }
    }
}

netParams.cellParams['STN'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 60,
                "L": 60,
                "Ra": 200.0,
                "cm": 1
            },
            "mechs": {
                'myions': {},
                "stn": {
                    "gnabar": 49e-3,
                    "gkdrbar": 57e-3,
                    "gkabar": 5e-3, 
                    "gkcabar": 0.7e-3, #changed to hahn
                    "gcalbar": 15e-3,
					"gcatbar": 5e-3, 
                    "kca": 2, 
                    "gl": 0.29e-3 #changed to hahn
                }
            }
        }
    }
}

#%% Create populations

pop_Size=10

netParams.popParams['GPe_pop'] = {
    "cellModel": "",
    "cellType": 'GPe',
    "numCells": pop_Size,
    "yRange": [
        250,
        750
    ],
    "xRange": [
        0,
        250
    ],
    "zRange": [
        0,
        100
    ]
}

netParams.popParams['GPi_pop'] = {
    "cellModel": "",
    "cellType": 'GPe',
    "numCells": pop_Size,
    "yRange": [
        0,
        500
    ],
    "xRange": [
        250,
        750
    ],
    "zRange": [
        0,
        100
    ]
}

netParams.popParams['STN_pop'] = {
    "cellModel": "",
    "cellType": 'STN',
    "numCells": pop_Size,
    "yRange": [
        0,
        500
    ],
    "xRange": [
        0,
        500
    ],
    "zRange": [
        0,
        100
    ]
}

#%% Add stimulus
#check out amplitude again!! #currently from fleming
netParams.stimSourceParams['bias_gpe'] = {'type': 'IClamp', 'del': 0, 'dur': 1e12, 'amp':-0.009}
netParams.stimSourceParams['bias_gpi'] = {'type': 'IClamp', 'del': 0, 'dur': 1e12, 'amp': 0.006}
netParams.stimSourceParams['bias_stn'] = {'type': 'IClamp', 'del': 0, 'dur': 1e12, 'amp': -0.125}

#%% Add target
netParams.stimTargetParams['bias_gpe->gpe'] = {'source': 'bias_gpe','sec':'soma', 'loc': 0.5, 'conds': {'pop':'GPe_pop'}}
netParams.stimTargetParams['bias_gpi->gpi'] = {'source': 'bias_gpi','sec':'soma', 'loc': 0.5, 'conds': {'pop':'GPi_pop'}}
netParams.stimTargetParams['bias_stn->stn'] = {'source': 'bias_stn','sec':'soma', 'loc': 0.5, 'conds': {'pop':'STN_pop'}}

#%% Synaptic mechanism parameters - taken from fleming
netParams.synMechParams['AMPA'] = {'mod': 'AMPA_S'}  # excitatory synaptic mechanism
netParams.synMechParams['GABA'] = {'mod': 'GABAa_S'}  # inhibitory synaptic mechanism

#%% Connections - change connectivity rules, now 1 to 1!!!!
netParams.connParams['STN->GPe'] = {
    'preConds': {'pop': 'STN_pop'}, 
    'postConds': {'pop': 'GPe_pop'},
    'weight': 0.111111,
    'convergence': 1, 
    'sec': 'soma',
    'loc': 0.5,
    'synMech': 'AMPA',
    'delay': 4}

netParams.connParams['STN->GPi'] = {
    'preConds': {'pop': 'STN_pop'}, 
    'postConds': {'pop': 'GPi_pop'},
    'weight': 0.111111,
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'AMPA',
    'delay': 2}

netParams.connParams['GPe->GPi'] = {
    'preConds': {'pop': 'GPe_pop'}, 
    'postConds': {'pop': 'GPi_pop'},
    'weight': 0.111111,
    'convergence': 1,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': 'GABA',
    'delay': 2}

netParams.connParams['GPe->STN'] = {
    'preConds': {'pop': 'GPe_pop'}, 
    'postConds': {'pop': 'STN_pop'},
    'weight': 0.111111,
    'convergence': 2,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': 'GABA',
    'delay': 3}

#change weight for parkinsonian state
netParams.connParams['GPe->GPe'] = {
    'preConds': {'pop': 'GPe_pop'}, 
    'postConds': {'pop': 'GPe_pop'},
    'weight': 0.015, #0.005
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'GABA',
    'delay': 4}

#%% cfg  
cfg = specs.SimConfig()					            # object of class SimConfig to store simulation configuration
cfg.duration = 1*1e3 						            # Duration of the simulation, in ms
cfg.dt = 0.01								                # Internal integration timestep to use
cfg.verbose = 0						                # Show detailed messages 
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
cfg.recordStep = 0.01 			
cfg.filename = 'model_output'  			# Set file output name
cfg.saveJson = False
cfg.analysis['plotTraces'] = {'include': [0,pop_Size,2*pop_Size]} # Plot recorded traces for this list of cells
cfg.hParams['celsius'] = 36
cfg.hParams['v_init'] = -68

#%% run
sim.createSimulateAnalyze(netParams = netParams, simConfig = cfg)
sim.analysis.plot2Dnet(include = ['GPe_pop','STN_pop', 'GPi_pop']);
sim.analysis.plotSpikeStats(include = ['GPe_pop','STN_pop', 'GPi_pop'], saveFig=False);
#sim.analysis.plotRateSpectrogram(include=['GPi_pop']);