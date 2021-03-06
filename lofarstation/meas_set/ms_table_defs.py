#!/usr/bin/env python

import numpy as np

ms_table_defs = {
"MAIN":
  {"info": {'readme': 'This is a MeasurementSet Table holding measurements from a Telescope\n', 'subType': '', 'type': 'Measurement Set'},
   "desc": {'ARRAY_ID': {'comment': 'ID of array or subarray', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'},
            'OBSERVATION_ID': {'comment': 'ID for this observation, index in OBSERVATION table', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'},
            'STATE_ID': {'comment': 'ID for this observing state', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'},
            'SIGMA': {'comment': 'Estimated rms noise for channel with unity bandpass response', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'float', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            'EXPOSURE': {'comment': 'The effective integration time', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'PROCESSOR_ID': {'comment': 'Id for backend processor, index in PROCESSOR table', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'INTERVAL': {'comment': 'The sampling interval', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'UVW': {'comment': 'Vector with uvw coordinates (in meters)', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 5, 'valueType': 'double', 'maxlen': 0, 'shape': np.array([3], dtype=np.int32), 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            'FEED1': {'comment': 'The feed index for ANTENNA1', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            '_define_hypercolumn_': {},
            'TIME_CENTROID': {'comment': 'Modified Julian Day', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'},
            'WEIGHT': {'comment': 'Weight for each polarization spectrum', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'float', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            'FLAG': {'comment': 'The data flags, array of bools with same shape as data', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'boolean', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 2}, 
            'FLAG_CATEGORY': {'comment': 'The flag category, NUM_CAT flags for each datum', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'boolean', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 3}, 
            'FLAG_ROW': {'comment': 'Row flag - flag all data in this row if True', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'boolean', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'FEED2': {'comment': 'The feed index for ANTENNA2', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'FIELD_ID': {'comment': 'Unique id for this pointing', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'DATA_DESC_ID': {'comment': 'The data description table index', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'TIME': {'comment': 'Modified Julian Day', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'ANTENNA2': {'comment': 'ID of second antenna in interferometer', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'ANTENNA1': {'comment': 'ID of first antenna in interferometer', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'SCAN_NUMBER': {'comment': 'Sequential scan number from on-line system', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'},
            'DATA': {'comment': 'The data column', 'dataManagerType': 'TiledShapeStMan', '_c_order': True, 'option': 0, 'valueType': 'complex', 'maxlen': 0, 'dataManagerGroup': 'TiledData', 'ndim': 2}
           },
   "col_keywords": {'TIME': {'QuantumUnits': ['s'], 
                    'MEASINFO': {'Ref': 'UTC', 'type': 'epoch'}}, 
                    'INTERVAL': {'QuantumUnits': ['s']}, 
                    'TIME_CENTROID': {'QuantumUnits': ['s'], 'MEASINFO': {'Ref': 'UTC', 'type': 'epoch'}}, 
                    'UVW': {'QuantumUnits': ['m', 'm', 'm'], 'MEASINFO': {'Ref': 'ITRF', 'type': 'uvw'}}, 
                    'FLAG_CATEGORY': {'CATEGORY': []}, 
                    'EXPOSURE': {'QuantumUnits': ['s']}},
   "keywords": {'MS_VERSION': np.float32(2)}
  },
"FEED":
  {"info": {'readme': '', 'subType': '', 'type': ''},
   "desc": {'NUM_RECEPTORS': {'comment': 'Number of receptors on this feed (probably 1 or 2)', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'},
            'SPECTRAL_WINDOW_ID': {'comment': 'ID for this spectral window setup', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'RECEPTOR_ANGLE': {'comment': 'The reference angle for polarization', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            'INTERVAL': {'comment': 'Interval for which this set of parameters is accurate', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'POL_RESPONSE': {'comment': 'D-matrix i.e. leakage between two receptors', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'complex', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 2}, 
            'TIME': {'comment': 'Midpoint of time for which this set of parameters is accurate', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'POLARIZATION_TYPE': {'comment': 'Type of polarization to which a given RECEPTOR responds', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            'FEED_ID': {'comment': 'Feed id', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'ANTENNA_ID': {'comment': 'ID of antenna in this array', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'BEAM_ID': {'comment': 'Id for BEAM model', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'POSITION': {'comment': 'Position of feed relative to feed reference position', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 5, 'valueType': 'double', 'maxlen': 0, 'shape': np.array([3], dtype=np.int32), 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            'BEAM_OFFSET': {'comment': 'Beam position offset (on sky but in antennareference frame)', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 2}, 
            '_define_hypercolumn_': {}},
   "col_keywords": {'RECEPTOR_ANGLE': {'QuantumUnits': ['rad']}, 
                    'INTERVAL': {'QuantumUnits': ['s']}, 
                    'TIME': {'QuantumUnits': ['s'], 'MEASINFO': {'Ref': 'UTC', 'type': 'epoch'}}, 
                    'POSITION': {'QuantumUnits': ['m', 'm', 'm'], 'MEASINFO': {'Ref': 'ITRF', 'type': 'position'}}, 
                    'BEAM_OFFSET': {'QuantumUnits': ['rad', 'rad'], 'MEASINFO': {'Ref': 'J2000', 'type': 'direction'}}},
   "keywords": {}
  },
"SPECTRAL_WINDOW":
  {"info": {'readme': '', 'subType': '', 'type': ''},
   "desc": {'MEAS_FREQ_REF': {'comment': 'Frequency Measure reference', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'REF_FREQUENCY': {'comment': 'The reference frequency', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'EFFECTIVE_BW': {'comment': 'Effective noise bandwidth of each channel', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            'FREQ_GROUP': {'comment': 'Frequency group', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'TOTAL_BANDWIDTH': {'comment': 'The total bandwidth for this window', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'NAME': {'comment': 'Spectral window name', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'CHAN_WIDTH': {'comment': 'Channel width for each channel', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            'NUM_CHAN': {'comment': 'Number of spectral channels', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'CHAN_FREQ': {'comment': 'Center frequencies for each channel in the data matrix', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            'IF_CONV_CHAIN': {'comment': 'The IF conversion chain number', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'NET_SIDEBAND': {'comment': 'Net sideband', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            '_define_hypercolumn_': {}, 
            'FREQ_GROUP_NAME': {'comment': 'Frequency group name', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'RESOLUTION': {'comment': 'The effective noise bandwidth for each channel', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            'FLAG_ROW': {'comment': 'Row flag', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'boolean', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}},
   "col_keywords": {'MEAS_FREQ_REF': {}, 
                    'REF_FREQUENCY': {'QuantumUnits': ['Hz'], 'MEASINFO': {'TabRefTypes': ['REST', 'LSRK', 'LSRD', 'BARY', 'GEO', 'TOPO', 'GALACTO', 'LGROUP', 'CMB', 'Undefined'], 'type': 'frequency', 'VarRefCol': 'MEAS_FREQ_REF', 'TabRefCodes': np.array([ 0,  1,  2,  3,  4,  5,  6,  7,  8, 64], dtype=np.uint32)}}, 
                    'EFFECTIVE_BW': {'QuantumUnits': ['Hz']}, 
                    'TOTAL_BANDWIDTH': {'QuantumUnits': ['Hz']}, 
                    'CHAN_WIDTH': {'QuantumUnits': ['Hz']}, 
                    'CHAN_FREQ': {'QuantumUnits': ['Hz'], 'MEASINFO': {'TabRefTypes': ['REST', 'LSRK', 'LSRD', 'BARY', 'GEO', 'TOPO', 'GALACTO', 'LGROUP', 'CMB', 'Undefined'], 'type': 'frequency', 'VarRefCol': 'MEAS_FREQ_REF', 'TabRefCodes': np.array([ 0,  1,  2,  3,  4,  5,  6,  7,  8, 64], dtype=np.uint32)}}, 
                    'RESOLUTION': {'QuantumUnits': ['Hz']}},
   "keywords": {}
  },
"DATA_DESCRIPTION":
  {"info": {'readme': '', 'subType': '', 'type': ''},
   "desc": {'SPECTRAL_WINDOW_ID': {'comment': 'Pointer to spectralwindow table', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            '_define_hypercolumn_': {}, 
            'POLARIZATION_ID': {'comment': 'Pointer to polarization table', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'FLAG_ROW': {'comment': 'Flag this row', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'boolean', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}},
   "col_keywords": {},
   "keywords": {}
  },
"OBSERVATION":
  {"info": {'readme': '', 'subType': '', 'type': ''},
   "desc": {'TELESCOPE_NAME': {'comment': 'Telescope Name (e.g. WSRT, VLBA)', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'LOG': {'comment': 'Observing log', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            'OBSERVER': {'comment': 'Name of observer(s)', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'SCHEDULE': {'comment': 'Observing schedule', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            'RELEASE_DATE': {'comment': 'Release date when data becomes public', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'TIME_RANGE': {'comment': 'Start and end of observation', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 5, 'valueType': 'double', 'maxlen': 0, 'shape': np.array([2], dtype=np.int32), 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            'PROJECT': {'comment': 'Project identification string', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            '_define_hypercolumn_': {}, 
            'SCHEDULE_TYPE': {'comment': 'Observing schedule type', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'FLAG_ROW': {'comment': 'Row flag', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'boolean', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}},
   "col_keywords": {'RELEASE_DATE': {'QuantumUnits': ['s'], 'MEASINFO': {'Ref': 'UTC', 'type': 'epoch'}}, 
                    'TIME_RANGE': {'QuantumUnits': ['s'], 'MEASINFO': {'Ref': 'UTC', 'type': 'epoch'}}},
   "keywords": {}
  },
"ANTENNA":
  {"info": {'readme': '', 'subType': '', 'type': ''},
   "desc": {'NAME': {'comment': 'Antenna name, e.g. VLA22, CA03', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'MOUNT': {'comment': 'Mount type e.g. alt-az, equatorial, etc.', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'OFFSET': {'comment': 'Axes offset of mount to FEED REFERENCE point', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 5, 'valueType': 'double', 'maxlen': 0, 'shape': np.array([3], dtype=np.int32), 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            'STATION': {'comment': 'Station (antenna pad) name', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'DISH_DIAMETER': {'comment': 'Physical diameter of dish', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'POSITION': {'comment': 'Antenna X,Y,Z phase reference position', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 5, 'valueType': 'double', 'maxlen': 0, 'shape': np.array([3], dtype=np.int32), 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            '_define_hypercolumn_': {}, 
            'TYPE': {'comment': 'Antenna type (e.g. SPACE-BASED)', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'FLAG_ROW': {'comment': 'Flag for this row', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'boolean', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}},
   "col_keywords": {'OFFSET': {'QuantumUnits': ['m', 'm', 'm'], 'MEASINFO': {'Ref': 'ITRF', 'type': 'position'}}, 
                    'DISH_DIAMETER': {'QuantumUnits': ['m']}, 
                    'POSITION': {'QuantumUnits': ['m', 'm', 'm'], 'MEASINFO': {'Ref': 'ITRF', 'type': 'position'}}},
   "keywords": {}
  },
"HISTORY":
  {"info": {'readme': '', 'subType': '', 'type': ''},
   "desc": {'ORIGIN': {'comment': '(Source code) origin from which message originated', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'APP_PARAMS': {'comment': 'Application parameters', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            'OBSERVATION_ID': {'comment': 'Observation id (index in OBSERVATION table)', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'TIME': {'comment': 'Timestamp of message', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'OBJECT_ID': {'comment': 'Originating ObjectID', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'PRIORITY': {'comment': 'Message priority', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'APPLICATION': {'comment': 'Application name', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'CLI_COMMAND': {'comment': 'CLI command sequence', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            'MESSAGE': {'comment': 'Log message', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            '_define_hypercolumn_': {}},
   "col_keywords": {'TIME': {'QuantumUnits': ['s'], 
                    'MEASINFO': {'Ref': 'UTC', 'type': 'epoch'}}},
   "keywords": {}
  },
"POLARIZATION":
  {"info": {'readme': '', 'subType': '', 'type': ''},
   "desc": {'CORR_TYPE': {'comment': 'The polarization type for each correlation product, as a Stokes enum.', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 1}, 
            'CORR_PRODUCT': {'comment': 'Indices describing receptors of feed going into correlation', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 2}, 
            '_define_hypercolumn_': {}, 
            'NUM_CORR': {'comment': 'Number of correlation products', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'FLAG_ROW': {'comment': 'Row flag', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'boolean', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}},
   "col_keywords": {},
   "keywords": {}
  },
"FIELD":
  {"info": {'readme': '', 'subType': '', 'type': ''},
   "desc": {'REFERENCE_DIR': {'comment': 'Direction of REFERENCE center (e.g. RA, DEC).as polynomial in time.', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 2}, 
            'CODE': {'comment': 'Special characteristics of field, e.g. Bandpass calibrator', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'NAME': {'comment': 'Name of this field', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'PHASE_DIR': {'comment': 'Direction of phase center (e.g. RA, DEC).', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 2}, 
            'DELAY_DIR': {'comment': 'Direction of delay center (e.g. RA, DEC)as polynomial in time.', 'dataManagerType': 'StandardStMan', '_c_order': True, 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan', 'ndim': 2}, 
            'TIME': {'comment': 'Time origin for direction and rate', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'SOURCE_ID': {'comment': 'Source id', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            '_define_hypercolumn_': {}, 
            'NUM_POLY': {'comment': 'Polynomial order of _DIR columns', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'FLAG_ROW': {'comment': 'Row Flag', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'boolean', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}},
   "col_keywords": {'REFERENCE_DIR': {'QuantumUnits': ['rad', 'rad'], 'MEASINFO': {'Ref': 'J2000', 'type': 'direction'}}, 
                    'PHASE_DIR': {'QuantumUnits': ['rad', 'rad'], 'MEASINFO': {'Ref': 'J2000', 'type': 'direction'}}, 
                    'DELAY_DIR': {'QuantumUnits': ['rad', 'rad'], 'MEASINFO': {'Ref': 'J2000', 'type': 'direction'}}, 
                    'TIME': {'QuantumUnits': ['s'], 'MEASINFO': {'Ref': 'UTC', 'type': 'epoch'}}},
   "keywords": {}
  },
"STATE":
  {"info": {'readme': '', 'subType': '', 'type': ''},
   "desc": {'LOAD': {'comment': 'Load temperature', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'OBS_MODE': {'comment': 'Observing mode, e.g., OFF_SPECTRUM', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'SUB_SCAN': {'comment': 'Sub scan number, relative to scan number', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'SIG': {'comment': 'True for a source observation', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'boolean', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'CAL': {'comment': 'Noise calibration temperature', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            '_define_hypercolumn_': {}, 
            'REF': {'comment': 'True for a reference observation', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'boolean', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'FLAG_ROW': {'comment': 'Row flag', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'boolean', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}},
   "col_keywords": {'LOAD': {'QuantumUnits': ['K']},
                    'CAL': {'QuantumUnits': ['K']}},
   "keywords": {}
  },
"POINTING":
  {"info": {'readme': '', 'subType': '', 'type': ''},
   "desc": {'DIRECTION': {'comment': 'Antenna pointing direction as polynomial in time', 'dataManagerType': 'IncrementalStMan', '_c_order': True, 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'ISMPointing', 'ndim': 2}, 
            'TRACKING': {'comment': 'Tracking flag - True if on position', 'dataManagerType': 'IncrementalStMan', 'option': 0, 'valueType': 'boolean', 'maxlen': 0, 'dataManagerGroup': 'ISMPointing'}, 
            'TARGET': {'comment': 'target direction as polynomial in time', 'dataManagerType': 'IncrementalStMan', '_c_order': True, 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'ISMPointing', 'ndim': -1}, 
            'TIME_ORIGIN': {'comment': 'Time origin for direction', 'dataManagerType': 'IncrementalStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'ISMPointing'}, 
            'INTERVAL': {'comment': 'Time interval', 'dataManagerType': 'IncrementalStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'ISMPointing'}, 
            'TIME': {'comment': 'Time interval midpoint', 'dataManagerType': 'IncrementalStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'ISMPointing'}, 
            'ANTENNA_ID': {'comment': 'Antenna Id', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'SSMPointing'}, 
            '_define_hypercolumn_': {}, 
            'NUM_POLY': {'comment': 'Series order', 'dataManagerType': 'IncrementalStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'ISMPointing'}, 
            'NAME': {'comment': 'Pointing position name', 'dataManagerType': 'IncrementalStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'ISMPointing'}},
   "col_keywords": {'DIRECTION': {'QuantumUnits': ['rad', 'rad'], 'MEASINFO': {'Ref': 'J2000', 'type': 'direction'}}, 
                    'TRACKING': {}, 'TARGET': {'QuantumUnits': ['rad', 'rad'], 'MEASINFO': {'Ref': 'J2000', 'type': 'direction'}}, 
                    'TIME_ORIGIN': {'QuantumUnits': ['s'], 'MEASINFO': {'Ref': 'UTC', 'type': 'epoch'}}, 
                    'INTERVAL': {'QuantumUnits': ['s']}, 'TIME': {'QuantumUnits': ['s'], 'MEASINFO': {'Ref': 'UTC', 'type': 'epoch'}}},
   "keywords": {}
  },
"PROCESSOR":
  {"info": {'readme': '', 'subType': '', 'type': ''},
   "desc": {'MODE_ID': {'comment': 'Processor mode id', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'TYPE_ID': {'comment': 'Processor type id', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            '_define_hypercolumn_': {}, 
            'TYPE': {'comment': 'Processor type', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'SUB_TYPE': {'comment': 'Processor sub type', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'FLAG_ROW': {'comment': 'Row flag', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'boolean', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}},
   "col_keywords": {},
   "keywords": {}
  },
"FLAG_CMD":
  {"info": {'readme': '', 'subType': '', 'type': ''},
   "desc": {'APPLIED': {'comment': 'True if flag has been applied to main table', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'boolean', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'SEVERITY': {'comment': 'Severity code (0-10) ', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'LEVEL': {'comment': 'Flag level - revision level ', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'int', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'INTERVAL': {'comment': 'Time interval for which this flag is valid', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'REASON': {'comment': 'Flag reason', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'COMMAND': {'comment': 'Flagging command', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            'TIME': {'comment': 'Midpoint of interval for which this flag is valid', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'double', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}, 
            '_define_hypercolumn_': {}, 
            'TYPE': {'comment': 'Type of flag (FLAG or UNFLAG)', 'dataManagerType': 'StandardStMan', 'option': 0, 'valueType': 'string', 'maxlen': 0, 'dataManagerGroup': 'StandardStMan'}},
   "col_keywords": {'INTERVAL': {'QuantumUnits': ['s']}, 
                    'TIME': {'QuantumUnits': ['s'], 'MEASINFO': {'Ref': 'UTC', 'type': 'epoch'}}},
   "keywords": {}
  }#,
#"SOURCE":
#  {"info": {"readme": "", "subType": "", "type": ""},
#   "desc": {"DIRECTION": {"comment": "Direction (e.g. RA, DEC).", "dataManagerType": "StandardStMan", "_c_order": True, "option": 5, "valueType": "double", "maxlen": 0, "shape": array([2], dtype=int32), "dataManagerGroup": "StandardStMan", "ndim": 1},
#            "CODE": {"comment": "Special characteristics of source, e.g. Bandpass calibrator", "dataManagerType": "StandardStMan", "option": 0, "valueType": "string", "maxlen": 0, "dataManagerGroup": "StandardStMan"},
#            "NAME": {"comment": "Name of source as given during observations", "dataManagerType": "StandardStMan", "option": 0, "valueType": "string", "maxlen": 0, "dataManagerGroup": "StandardStMan"},
#            "REST_FREQUENCY": {"comment": "Line rest frequency", "dataManagerType": "StandardStMan", "_c_order": True, "option": 0, "valueType": "double", "maxlen": 0, "dataManagerGroup": "StandardStMan", "ndim": -1},
#            "SPECTRAL_WINDOW_ID": {"comment": "ID for this spectral window setup", "dataManagerType": "StandardStMan", "option": 0, "valueType": "int", "maxlen": 0, "dataManagerGroup": "StandardStMan"}, 
#            "PROPER_MOTION": {"comment": "Proper motion", "dataManagerType": "StandardStMan", "_c_order": True, "option": 5, "valueType": "double", "maxlen": 0, "shape": array([2], dtype=int32), "dataManagerGroup": "StandardStMan", "ndim": 1}, 
#            "INTERVAL": {"comment": "Interval of time for which this set of parameters is accurate", "dataManagerType": "StandardStMan", "option": 0, "valueType": "double", "maxlen": 0, "dataManagerGroup": "StandardStMan"},
#            "SYSVEL": {"comment": "Systemic velocity at reference", "dataManagerType": "StandardStMan", "_c_order": True, "option": 0, "valueType": "double", "maxlen": 0, "dataManagerGroup": "StandardStMan", "ndim": -1},
#            "SOURCE_MODEL": {"comment": "Component Source Model", "dataManagerType": "StandardStMan", "option": 0, "valueType": "record", "maxlen": 0, "dataManagerGroup": "StandardStMan"},
#            "TIME": {"comment": "Midpoint of time for which this set of parameters is accurate.", "dataManagerType": "StandardStMan", "option": 0, "valueType": "double", "maxlen": 0, "dataManagerGroup": "StandardStMan"},
#            "SOURCE_ID": {"comment": "Source id", "dataManagerType": "StandardStMan", "option": 0, "valueType": "int", "maxlen": 0, "dataManagerGroup": "StandardStMan"},
#            "CALIBRATION_GROUP": {"comment": "Number of grouping for calibration purpose.", "dataManagerType": "StandardStMan", "option": 0, "valueType": "int", "maxlen": 0, "dataManagerGroup": "StandardStMan"},
#            "POSITION": {"comment": "Position (e.g. for solar system objects", "dataManagerType": "StandardStMan", "_c_order": True, "option": 0, "valueType": "double", "maxlen": 0, "dataManagerGroup": "StandardStMan", "ndim": -1},
#            "_define_hypercolumn_": {},
#            "TRANSITION": {"comment": "Line Transition name", "dataManagerType": "StandardStMan", "_c_order": True, "option": 0, "valueType": "string", "maxlen": 0, "dataManagerGroup": "StandardStMan", "ndim": -1},
#            "NUM_LINES": {"comment": "Number of spectral lines", "dataManagerType": "StandardStMan", "option": 0, "valueType": "int", "maxlen": 0, "dataManagerGroup": "StandardStMan"}},
#   "col_keywords": {"DIRECTION": {"QuantumUnits": ["rad", "rad"], "MEASINFO": {"Ref": "J2000", "type": "direction"}}, 
#                    "PROPER_MOTION": {"QuantumUnits": ["rad/s"]}, 
#                    "INTERVAL": {"QuantumUnits": ["s"]}, 
#                    "TIME": {"QuantumUnits": ["s"], "MEASINFO": {"Ref": "UTC", "type": "epoch"}}, 
#                    "SYSVEL": {"QuantumUnits": ["m/s"], "MEASINFO": {"Ref": "LSRK", "type": "radialvelocity"}}, 
#                    "REST_FREQUENCY": {"QuantumUnits": ["Hz"], "MEASINFO": {"Ref": "LSRK", "type": "frequency"}}, 
#                    "POSITION": {"QuantumUnits": ["m", "m", "m"], "MEASINFO": {"Ref": "ITRF", "type": "position"}}},
#   "keywords": {"model_0": 0, "definedmodel_field_0": "model_0"}
#  }
}
