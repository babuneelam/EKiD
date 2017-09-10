import os
import re

class AlgoCfg:
    AlgoType = 'Full'
    max_blank_chars = 0

    @classmethod
    def process_config_file(cls, algo_config_file):
        algo_f = open(algo_config_file)
        algo_cfgs = algo_f.readlines()

        for algo_cfg in algo_cfgs:
            algo_cfg = algo_cfg.rstrip()
            if algo_cfg == 'Full':
                cls.AlgoType = 'full'
                cls.max_blank_chars = 0
            elif algo_cfg == 'random':
                cls.AlgoType = 'Random'
            elif bool(re.match('^max_blank_chars=[0-9]+', algo_cfg)):
                cls.max_blank_chars = int(re.findall('\d+', algo_cfg)[0])
            elif algo_cfg == 'empty':
                cls.AlgoType = 'Empty'
                cls.max_blank_chars = 0
            elif algo_cfg == 'specified':
                cls.AlgoType = 'Specified'
                cls.max_blank_chars = 0
            elif algo_cfg == 'set':
                cls.AlgoType = 'Set'
            else:
               continue
	#print cls.max_blank_chars
	#print cls.AlgoType
 

