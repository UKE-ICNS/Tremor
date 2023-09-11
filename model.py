#This will be a file for a PD tremor project
import matplotlib
from netpyne import specs, sim 
from neuron import h
import numpy as np
import os
import winsound

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

#from fleming
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

#from santaniello
netParams.cellParams['Th'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 96,
                "L": 96,
                #"Ra": 200.0,
                "cm": 1
            },
            "mechs": {
                'tcfastNa': {},
                'tcslowK': {},
                'tcCaT': {},
                'tcCaConc': {},
                'tcfastK': {},
                'tch': {},
                'tcpas2': {}
            },
            'ions': {
                'na': {
                    'e': 45
                },
                'k': {
                    'e': -95
                }
            }
        }
    }
}

#from santaniello
netParams.cellParams['PYR'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 96,
                "L": 96,
                "Ra": 100.0,
                "cm": 1
            },
            "mechs": {
                'pas': {
                    'g': 1e-5,
                    'e': -85
                },
                'mchh2': {
                    "vtraub": -55,
                    'gnabar': 0.05,
                    'gkbar': 0.005
                },
                'mcIm': {
                    'tau_m': 1000,
                    'gkbar': 3e-5
                },
                'mcCad': {
                    'depth': 1,
                    'taur': 5,
                    'cainf': 2.4e-4,
                    'kt': 0
                },
                'mcIt': {
                    'gcabar': 4e-4
                }
            },
            'ions': {
                'na': {
                    'e': 50
                },
                'k': {
                    'e': -100
                },
                'ca': {
                    'cai': 2.4e-4,
                    'cao': 2,
                    'eca': 120
                }
            }
        }
    }
}

#from santaniello
netParams.cellParams['FSI'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 67,
                "L": 67,
                "Ra": 100.0,
                "cm": 1
            },
            "mechs": {
                'pas': {
                    'g': 0.00015,
                    'e': -70
                },
                'mchh2': {
                    "vtraub": -55,
                    'gnabar': 0.05,
                    'gkbar': 0.01
                }
            },
            'ions': {
                'na': {
                    'e': 50
                },
                'k': {
                    'e': -100
                }
            }
        }
    }
}

#dummy izhi - size like gpe
netParams.cellParams['Str'] = {
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
            "pointps": {
                "Izhi": { #???
                    'mod': 'Izhi2007b',
                    'C':1,
                    'k':0.7,
                    'vr':-60,
                    'vt':-40,
                    'vpeak':35,
                    'a':0.03, 
                    'b':-2,
                    'c':-50,
                    'd':100,
                    'celltype':1
                }
            }
        }
    }
}

#dummy izhi - size like santaniello
netParams.cellParams['Cer_nuc'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 20.248,
                "L": 65,
                "Ra": 35.4,
                "cm": 1
            },
            "pointps": {
                "Izhi": { #???
                    'mod': 'Izhi2007b',
                    'C':1,
                    'k':0.7,
                    'vr':-60,
                    'vt':-40,
                    'vpeak':35,
                    'a':0.03,
                    'b':-2,
                    'c':-50,
                    'd':100,
                    'celltype':1
                }
            }
        }
    }
}

#like santaniello
netParams.cellParams['Cer_ctx'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 20,
                "L": 20,
                #"Ra": 200.0,
                "cm": 1
            },
            "mechs": {
                'pcNarsg': {
                    'gbar': 0.016
                },
                'pcKv1': {
                    'gbar': 0.011
                },
                'pcKv4': {
                    'gbar': 0.0039
                },
                'pcKbin': {
                    'gbar': 0.0016
                },
                'pcCaBK': {
                    'gkbar': 0.014
                },
                'pcCaint': {},
                'pcCaP': {
                    'pcabar': 0.00006
                },
                'pcIhcn': {
                    "ghbar": 0.0002,
                    "eh": -30
                },
                'pcleak': {
                    "gbar": 9e-5,
                    "e": -61
                },
                'pcNa': {
                    'gbar': 0.014
                }
            },
            'threshold': 3,
            'ions': {
                'na': {
                    'e': 60
                },
                'k': {
                    'e': -88
                },
                'ca': {
                    'cao': 2
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
        250,
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

#add some noise in th! 
netParams.popParams['VLA_pop'] = {
    "cellModel": "",
    "cellType": 'Th',
    "numCells": pop_Size,
    "yRange": [
        250,
        500
    ],
    "xRange": [
        750,
        825
    ],
    "zRange": [
        0,
        100
    ]
}

#add some noise in th! 
netParams.popParams['VLP_pop'] = {
    "cellModel": "",
    "cellType": 'Th',
    "numCells": pop_Size,
    "yRange": [
        250,
        500
    ],
    "xRange": [
        825,
        1000
    ],
    "zRange": [
        0,
        100
    ]
}

#noise in ctx?
netParams.popParams['PYR_pop'] = {
    "cellModel": "",
    "cellType": 'PYR',
    "numCells": 20*pop_Size, #scale to santaniello
    "yRange": [
        0,
        250
    ],
    "xRange": [
        0,
        1000
    ],
    "zRange": [
        0,
        100
    ]
}

#noise in ctx?
netParams.popParams['FSI_pop'] = {
    "cellModel": "",
    "cellType": 'FSI',
    "numCells": 2*pop_Size, #scale to santaniello
    "yRange": [
        0,
        250
    ],
    "xRange": [
        0,
        1000
    ],
    "zRange": [
        0,
        100
    ]
}

#dummy
netParams.popParams['Str_pop'] = {
    "cellModel": "",
    "cellType": 'Str',
    "numCells": pop_Size,
    "yRange": [
        250,
        500
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

#dummy
netParams.popParams['Cern_pop'] = {
    "cellModel": "",
    "cellType": 'Cer_nuc',
    "numCells": pop_Size, #scale to santaniello
    "yRange": [
        750,
        1000
    ],
    "xRange": [
        750,
        850
    ],
    "zRange": [
        0,
        100
    ]
}

#dummy
netParams.popParams['Cerc_pop'] = {
    "cellModel": "",
    "cellType": 'Cer_ctx',
    "numCells": 40*pop_Size, #scale from santaniello
    "yRange": [
        750,
        1000
    ],
    "xRange": [
        850,
        1000
    ],
    "zRange": [
        0,
        100
    ]
}

#HERE
#add some noise in th! 
netParams.popParams['TRN_pop'] = {
    "cellModel": "",
    "cellType": 'Th',
    "numCells": pop_Size,
    "yRange": [
        250,
        500
    ],
    "xRange": [
        825,
        1000
    ],
    "zRange": [
        0,
        100
    ]
}

#%% Add stimulus
#check out amplitude again!! #currently from fleming biases, for tc,ctx,cern,cerc? biases from santaniello
netParams.stimSourceParams['bias_gpe'] = {'type': 'IClamp', 'del': 0, 'dur': 1e12, 'amp': 0}
netParams.stimSourceParams['bias_gpi'] = {'type': 'IClamp', 'del': 0, 'dur': 1e12, 'amp': 0.1}
netParams.stimSourceParams['bias_stn'] = {'type': 'IClamp', 'del': 0, 'dur': 1e12, 'amp': 0} 
netParams.stimSourceParams['bias_pyr'] = {'type': 'IClamp', 'del': 0, 'dur': 1e10, 'amp': 0.17} #5Hz
netParams.stimSourceParams['bias_fsi'] = {'type': 'IClamp', 'del': 0, 'dur': 1e10, 'amp': 0.15} #17Hz
netParams.stimSourceParams['bias_cern'] = {'type': 'IClamp', 'del': 0, 'dur': 1e10, 'amp': 0.5} #26Hz
netParams.stimSourceParams['bias_cerc'] = {'type': 'IClamp', 'del': 0, 'dur': 1e10, 'amp': 0.001} #40-50 Hz
netParams.stimSourceParams['bias_str'] = {'type': 'IClamp', 'del': 0, 'dur': 1e10, 'amp': 0.05}
#%% Add target
netParams.stimTargetParams['bias_gpe->gpe'] = {'source': 'bias_gpe','sec':'soma', 'loc': 0.5, 'conds': {'pop':'GPe_pop'}}
netParams.stimTargetParams['bias_gpi->gpi'] = {'source': 'bias_gpi','sec':'soma', 'loc': 0.5, 'conds': {'pop':'GPi_pop'}}
netParams.stimTargetParams['bias_stn->stn'] = {'source': 'bias_stn','sec':'soma', 'loc': 0.5, 'conds': {'pop':'STN_pop'}}
netParams.stimTargetParams['bias_pyr->pyr'] = {'source': 'bias_pyr','sec':'soma', 'loc': 0.5, 'conds': {'pop':'PYR_pop'}}
netParams.stimTargetParams['bias_fsi->fsi'] = {'source': 'bias_fsi','sec':'soma', 'loc': 0.5, 'conds': {'pop':'FSI_pop'}}
netParams.stimTargetParams['bias_cern->cern'] = {'source': 'bias_cern','sec':'soma', 'loc': 0.5, 'conds': {'pop':'Cern_pop'}}
netParams.stimTargetParams['bias_cerc->cerc'] = {'source': 'bias_cerc','sec':'soma', 'loc': 0.5, 'conds': {'pop':'Cerc_pop'}}
netParams.stimTargetParams['bias_str->str'] = {'source': 'bias_str','sec':'soma', 'loc': 0.5, 'conds': {'pop':'Str_pop'}}
#%% Synaptic mechanism parameters - taken from fleming
netParams.synMechParams['AMPA'] = {'mod': 'AMPA_S'}  # excitatory synaptic mechanism
netParams.synMechParams['GABA'] = {'mod': 'GABAa_S'}  # inhibitory synaptic mechanism

#%% Connections - change connectivity rules, now 1 to 1!!!! from fleming
DA = 0.1

cd2 = 0.1
Ad1 = 10
Ad2 = 7.5
lam = 7.5
cD1 = Ad1/(1+np.exp(-lam*(DA-1)))
cD2 = Ad2/(1+np.exp(lam*(DA))) 

netParams.connParams['STN->GPe'] = {
    'preConds': {'pop': 'STN_pop'}, 
    'postConds': {'pop': 'GPe_pop'},
    'weight': 0.271111*(1-cd2*DA),
    'convergence': 1, 
    'sec': 'soma',
    'loc': 0.5,
    'synMech': 'AMPA',
    'delay': 4}

netParams.connParams['STN->GPi'] = {
    'preConds': {'pop': 'STN_pop'}, 
    'postConds': {'pop': 'GPi_pop'},
    'weight': 0.45,
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
    'weight': 0.211111*(1-cd2*DA),
    'convergence': 2,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': 'GABA',
    'delay': 3}

#change weight for parkinsonian state
netParams.connParams['GPe->GPe'] = {
    'preConds': {'pop': 'GPe_pop'}, 
    'postConds': {'pop': 'GPe_pop'},
    'weight': 0.0197/DA,#0.015, #pd 0.11 #cool 0.16 ;1, 0.012? #HERE
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'GABA',
    'delay': 4}

netParams.connParams['GPi->VLA'] = {
    'preConds': {'pop': 'GPi_pop'}, 
    'postConds': {'pop': 'VLA_pop'},
    'weight': 3,
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'GABA',
    'delay': 2}

#change this!!!! for now like fleming but div from santaniello
netParams.connParams['VLA->PYR'] = {
    'preConds': {'pop': 'VLA_pop'}, 
    'postConds': {'pop': 'PYR_pop'},
    'weight': 5, 
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 6,
    'synMech': 'AMPA',
    'delay': 2}

netParams.connParams['VLA->FSI'] = {
    'preConds': {'pop': 'VLA_pop'}, 
    'postConds': {'pop': 'FSI_pop'},
    'weight': 5, #same as backwards but 16 times smaller #HERE
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 2,
    'synMech': 'AMPA',
    'delay': 4} #2 times bigger

netParams.connParams['VLP->PYR'] = {
    'preConds': {'pop': 'VLP_pop'}, 
    'postConds': {'pop': 'PYR_pop'},
    'weight': 5,
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 6,
    'synMech': 'AMPA',
    'delay': 2}

netParams.connParams['VLP->FSI'] = {
    'preConds': {'pop': 'VLP_pop'}, 
    'postConds': {'pop': 'FSI_pop'},
    'weight': 5, #same as backwards but 16 times smaller #HERE
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 2,
    'synMech': 'AMPA',
    'delay': 4} #2 times bigger

#HERE
netParams.connParams['VLA->TRN'] = {
    'preConds': {'pop': 'VLA_pop'}, 
    'postConds': {'pop': 'TRN_pop'},
    'weight': 0.02, 
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'AMPA',
    'delay': 3}

netParams.connParams['VLP->TRN'] = {
    'preConds': {'pop': 'VLP_pop'}, 
    'postConds': {'pop': 'TRN_pop'},
    'weight': 0.02, 
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'AMPA',
    'delay': 3}

netParams.connParams['TRN->VLA'] = {
    'preConds': {'pop': 'TRN_pop'}, 
    'postConds': {'pop': 'VLA_pop'},
    'weight': 0.4, 
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'GABA',
    'delay': 3}

netParams.connParams['TRN->VLP'] = {
    'preConds': {'pop': 'TRN_pop'}, 
    'postConds': {'pop': 'VLP_pop'},
    'weight': 0.4, 
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'GABA',
    'delay': 3}

netParams.connParams['TRN->TRN'] = {
    'preConds': {'pop': 'TRN_pop'}, 
    'postConds': {'pop': 'TRN_pop'},
    'weight': 0.4, 
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'GABA',
    'delay': 3}

netParams.connParams['PYR->VLA'] = {
    'preConds': {'pop': 'PYR_pop'}, 
    'postConds': {'pop': 'VLA_pop'},
    'weight': 1, # same as backwards but 16 times smaller #HERE
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 4,
    'synMech': 'AMPA',
    'delay': 2}

netParams.connParams['PYR->VLP'] = {
    'preConds': {'pop': 'PYR_pop'}, 
    'postConds': {'pop': 'VLP_pop'},
    'weight': 0.3, # same as backwards but 16 times smaller
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 4,
    'synMech': 'AMPA',
    'delay': 2}

#HERE
netParams.connParams['PYR->TRN'] = {
'preConds': {'pop': 'PYR_pop'}, 
'postConds': {'pop': 'TRN_pop'},
'weight': 0.03, # same as backwards but 16 times smaller
'sec': 'soma',
'loc': 0.5,
'convergence': 4,
'synMech': 'AMPA',
'delay': 2}

netParams.connParams['FSI->FSI'] = {
    'preConds': {'pop': 'FSI_pop'}, 
    'postConds': {'pop': 'FSI_pop'},
    'weight': 0.5, #same as backwards but 10 times smaller, maybe change to 11%??
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 19,
    'synMech': 'GABA',
    'delay': 0} #no delay

netParams.connParams['PYR->PYR'] = {
    'preConds': {'pop': 'PYR_pop'}, 
    'postConds': {'pop': 'PYR_pop'},
    'weight': 9, #same as backwards but 1.8 times bigger, maybe change to 20%??
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 5,
    'synMech': 'AMPA',
    'delay': 0} #no delay

netParams.connParams['PYR->FSI'] = {
    'preConds': {'pop': 'PYR_pop'}, 
    'postConds': {'pop': 'FSI_pop'},
    'weight': 0.8, #same as backwards but 6 times smaller also scaled, maybe change to 20%??
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 20*pop_Size,
    'synMech': 'AMPA',
    'delay': 0} #no delay

netParams.connParams['FSI->PYR'] = {
    'preConds': {'pop': 'FSI_pop'}, 
    'postConds': {'pop': 'PYR_pop'},
    'weight': 7.3, #santaniello scaled to fleming, maybe change to 10%??
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 20*pop_Size,
    'synMech': 'GABA',
    'delay': 0} #no delay

netParams.connParams['PYR->STN'] = {
    'preConds': {'pop': 'PYR_pop'}, 
    'postConds': {'pop': 'STN_pop'},
    'weight': 0.12, 
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 5,
    'synMech': 'AMPA',
    'delay': 1}

netParams.connParams['PYR->Str'] = {
    'preConds': {'pop': 'PYR_pop'}, 
    'postConds': {'pop': 'Str_pop'},
    'weight': 0.01*cD1,#0.01, #pd 0.003 #and as from str weight 1.42*0.003
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 5, #like to STN
    'synMech': 'AMPA',
    'delay': 1} #like to STN

netParams.connParams['Str->GPe'] = {
    'preConds': {'pop': 'Str_pop'}, 
    'postConds': {'pop': 'GPe_pop'},
    'weight': 0.01*cD2/Ad2, #fleming 
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1, #fleming
    'synMech': 'GABA',
    'delay': 1} #fleming

#taken from cern-vlp and as from str weight
netParams.connParams['Cern->Str'] = {
    'preConds': {'pop': 'Cern_pop'}, 
    'postConds': {'pop': 'Str_pop'},
    'weight': 0.01, 
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 1,
    'synMech': 'AMPA',
    'delay': 4} 

netParams.connParams['Cern->VLP'] = {
    'preConds': {'pop': 'Cern_pop'}, 
    'postConds': {'pop': 'VLP_pop'},
    'weight': 0.005, #santaniello scaled yo fleming 10 times smaller #HERE
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 1,
    'synMech': 'AMPA',
    'delay': 4} #santaniello 2 times more (scaled to fleming)

netParams.connParams['Cerc->Cern'] = {
    'preConds': {'pop': 'Cerc_pop'}, 
    'postConds': {'pop': 'Cern_pop'},
    'weight': 0.0017, #santaniello scaled to fleming
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 40,
    'synMech': 'GABA', #from santaniello scheme
    'delay': 8.4} #santaniello scaled 2 times more

#santaniello no scaling
netParams.connParams['PYR->Cerc'] = {
    'preConds': {'pop': 'PYR_pop'}, 
    'postConds': {'pop': 'Cerc_pop'},
    'weight': 3.49,#santaniello no scale
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 2.5, #cause there are gtl in between
    'synMech': 'AMPA',
    'delay': 4} #santaniello no scale

netParams.connParams['PYR->Cern'] = {
    'preConds': {'pop': 'PYR_pop'}, 
    'postConds': {'pop': 'Cern_pop'},
    'weight': 0.01, #as pyr-str
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 20, 
    'synMech': 'AMPA',
    'delay': 3.4} #santaniello scaled 2 times more

#taken from cern-vlp
netParams.connParams['STN->Cerc'] = {
    'preConds': {'pop': 'STN_pop'}, 
    'postConds': {'pop': 'Cerc_pop'},
    'weight': 0.01,
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 1,
    'synMech': 'AMPA',
    'delay': 4} 

#change weight for parkinsonian state
netParams.connParams['Str->Str'] = {
    'preConds': {'pop': 'Str_pop'}, 
    'postConds': {'pop': 'Str_pop'},
    'weight': 0.016, 
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'GABA',
    'delay': 4}
#What to do with striato-striatal connections?, now like for gpe
#%% cfg  
state="tr_try"
cfg = specs.SimConfig()					            # object of class SimConfig to store simulation configuration
cfg.duration = 1e3 						            # Duration of the simulation, in ms
cfg.dt = 0.01								                # Internal integration timestep to use
cfg.verbose = 0						                # Show detailed messages 
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
#cfg.recordTraces['dend_K'] =  { "sec": "soma", "loc": 0.0, "var": "ena"}
cfg.recordStep = 0.01 			
cfg.filename = f'{state}/model_output'  			# Set file output name
cfg.saveJson = True
cfg.analysis['plotRaster'] =  {'saveFig': f'{state}/raster.svg'}
cfg.analysis['plotTraces'] = {'include': [0,pop_Size,2*pop_Size,3*pop_Size,4*pop_Size,5*pop_Size,250,270,280,290,690]} # Plot recorded traces for this list of cells
cfg.hParams['celsius'] = 36
cfg.hParams['v_init'] = -68

#%% run
sim.createSimulateAnalyze(netParams = netParams, simConfig = cfg)
#%% plots
sim.analysis.plotSpikeHist(include = ['GPi_pop','VLP_pop','Cern_pop'], binSize=25, overlay=True, graphType='line',yaxis='rate',saveFig=f'{state}/spikehist.svg') # Plot recorded traces for this list of cells
sim.analysis.plotConn(includePre = ['GPe_pop','STN_pop','GPi_pop','VLA_pop','VLP_pop','PYR_pop','FSI_pop','Str_pop','Cern_pop','Cerc_pop','TRN_pop'], includePost = ['GPe_pop','STN_pop','GPi_pop','VLA_pop','VLP_pop','PYR_pop','FSI_pop','Str_pop','Cern_pop','Cerc_pop'],feature='numConns', graphType='bar',saveFig=f'{state}/numconns.svg')
#sim.analysis.plot2Dnet(include = ['GPe_pop','STN_pop','GPi_pop','VLA_pop','VLP_pop','PYR_pop','FSI_pop','Str_pop','Cern_pop','Cerc_pop','TRN_pop']);
sim.analysis.plotSpikeStats(include = ['GPe_pop','STN_pop','GPi_pop','VLA_pop','VLP_pop','PYR_pop','FSI_pop','Str_pop','Cern_pop','Cerc_pop','TRN_pop'],stats=['rate'],saveFig=f'{state}/rate.svg');
sim.analysis.plotSpikeStats(include = ['GPe_pop','STN_pop','GPi_pop','VLA_pop','VLP_pop','PYR_pop','FSI_pop','Str_pop','Cern_pop','Cerc_pop','TRN_pop'],stats=['isicv'],saveFig=f'{state}/isicv.svg');
sim.analysis.plotRateSpectrogram(include=['Cern_pop'], maxFreq=20, saveFig=f'{state}/cern.svg');
sim.analysis.plotRateSpectrogram(include=['Cern_pop'],saveFig=f'{state}/cern_enl.svg');
sim.analysis.plotRateSpectrogram(include=['STN_pop'],saveFig=f'{state}/stn.svg');
sim.analysis.plotRateSpectrogram(include=['STN_pop'], maxFreq=30,saveFig=f'{state}/stn_beta.svg');
sim.analysis.plotRateSpectrogram(include=['GPi_pop'],saveFig=f'{state}/gpi.svg');
sim.analysis.plotRateSpectrogram(include=['GPi_pop'], maxFreq=30,saveFig=f'{state}/gpi_beta.svg');
sim.analysis.plotRateSpectrogram(include=['GPe_pop'],saveFig=f'{state}/gpe.svg');
sim.analysis.plotRateSpectrogram(include=['GPe_pop'], maxFreq=30,saveFig=f'{state}/gpe_beta.svg');
sim.analysis.plotRateSpectrogram(include=['Cerc_pop'], maxFreq=20,saveFig=f'{state}/cerc_enl.svg');
sim.analysis.plotRateSpectrogram(include=['Cerc_pop'],saveFig=f'{state}/cerc.svg');
sim.analysis.plotRateSpectrogram(include=['VLP_pop'], maxFreq=20,saveFig=f'{state}/vlp_enl.svg');
sim.analysis.plotRateSpectrogram(include=['VLP_pop'],saveFig=f'{state}/vlp.svg');
sim.analysis.plotRateSpectrogram(include=['VLA_pop'], maxFreq=20,saveFig=f'{state}/vla_enl.svg');
sim.analysis.plotRateSpectrogram(include=['VLA_pop'],saveFig=f'{state}/vla.svg');
sim.analysis.plotRateSpectrogram(include=['TRN_pop'],saveFig=f'{state}/trn.svg');
sim.analysis.plotRateSpectrogram(include=['TRN_pop'], maxFreq=20,saveFig=f'{state}/trn_enl.svg');
sim.analysis.plotRateSpectrogram(include=['PYR_pop'],saveFig=f'{state}/pyr.svg');
sim.analysis.plotRateSpectrogram(include=['FSI_pop'],saveFig=f'{state}/fsi.svg');
sim.analysis.plotRateSpectrogram(include=['PYR_pop'], maxFreq=20,saveFig=f'{state}/pyr_enl.svg');
sim.analysis.plotRateSpectrogram(include=['FSI_pop'], maxFreq=20,saveFig=f'{state}/fsi_enl.svg');
#c,d=sim.analysis.plotRatePSD(include=[30,31,32,33,34,35,36,37,38,39],popColors=['b'],maxFreq=40,saveFig=f'{state}/vla_psd.svg');
c,d=sim.analysis.plotRatePSD(include=['VLA_pop'],popColors=['b'],maxFreq=40,saveFig=f'{state}/vla_psd.svg');
#e,ff=sim.analysis.plotRatePSD(include=[40,41,42,43,44,45,46,47,48,49],popColors=['b'],maxFreq=40,saveFig=f'{state}/vlp_psd.svg');
e,ff=sim.analysis.plotRatePSD(include=['VLP_pop'],popColors=['b'],maxFreq=40,saveFig=f'{state}/vlp_psd.svg');
#a,b=sim.analysis.plotRatePSD(include=[280,281,282,283,284,285,286,287,288,289],popColors=['b'],maxFreq=40,saveFig=f'{state}/cern_psd.svg');
a,b=sim.analysis.plotRatePSD(include=['Cern_pop'],popColors=['b'],maxFreq=40,saveFig=f'{state}/cern_psd.svg');
#g,h=sim.analysis.plotRatePSD(include=[10,11,12,13,14,15,16,17,18,19],popColors=['b'],maxFreq=40,saveFig=f'{state}/gpi_psd.svg');
g,h=sim.analysis.plotRatePSD(include=['GPi_pop'],popColors=['b'],maxFreq=40,saveFig=f'{state}/gpi_psd.svg');
#i,j=sim.analysis.plotRatePSD(include=[690,691,692,693,694,695,696,697,698,699],popColors=['b'],maxFreq=40,saveFig=f'{state}/trn_psd.svg');
i,j=sim.analysis.plotRatePSD(include=['TRN_pop'],popColors=['b'],maxFreq=40,saveFig=f'{state}/trn_psd.svg');

import pickle 

with open(f'{state}/trn_psd.pkl', 'wb') as f:
    pickle.dump(j, f)

with open(f'{state}/gpi_psd.pkl', 'wb') as f:
    pickle.dump(h, f)

with open(f'{state}/cern_psd.pkl', 'wb') as f:
    pickle.dump(b, f)

with open(f'{state}/vlp_psd.pkl', 'wb') as f:
    pickle.dump(ff, f)

with open(f'{state}/vla_psd.pkl', 'wb') as f:
    pickle.dump(d, f)

sim.analysis.popAvgRates()
#%%sound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
# winsound.Beep(frequency, duration)