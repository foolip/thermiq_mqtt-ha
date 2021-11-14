# ThermIQ generated register definitions
FIELD_REGNUM = 0
FIELD_REGTYPE = 1
FIELD_UNIT = 2
FIELD_MINVALUE = 3
FIELD_MAXVALUE = 4
FIELD_BITMASK = 3


# Register as sensors
reg_id = {
#  reg_id          : ['reg#' ],
  't_ute'              : ['r00', 'temperature',            'ºC',                           ],
  't_rum_ar'           : ['r01', 'temperature',            'ºC',                           ],
  't_rum_ar_dec'       : ['r02', 'temperature',            '0.1C',                          ],
  't_rum_bor'          : ['r03', 'temperature',            'ºC',                           ],
  't_rum_bor_dec'      : ['r04', 'temperature',            '0.1C',                          ],
  't_fram'             : ['r05', 'temperature',            'ºC',                           ],
  't_retur'            : ['r06', 'temperature',            'ºC',                           ],
  't_vatten'           : ['r07', 'temperature',            'ºC',                           ],
  't_brine_ut'         : ['r08', 'temperature',            'ºC',                           ],
  't_brine_in'         : ['r09', 'temperature',            'ºC',                           ],
  't_kylning'          : ['r0a', 'temperature',            'ºC',                           ],
  't_fram_shunt'       : ['r0b', 'temperature',            'ºC',                           ],
  'stromforbr'         : ['r0c', 'sensor',                 'A',                             ],
  'ts_1'               : ['r0d', 'binary_sensor',          'A',            0x0001           ],
  'ts_2'               : ['r0d', 'binary_sensor',          'A',            0x0002           ],
  't_fram_bor'         : ['r0e', 'temperature',            'ºC',                           ],
  't_fram_shunt_bor'   : ['r0f', 'temperature',            'ºC',                           ],
  'brine'              : ['r10', 'binary_sensor',          'ºC',          0x0001           ],
  'kompr'              : ['r10', 'binary_sensor',          'ºC',          0x0002           ],
  'cirkp'              : ['r10', 'binary_sensor',          'ºC',          0x0004           ],
  'varmvatten'         : ['r10', 'binary_sensor',          'ºC',          0x0008           ],
  'ts2'                : ['r10', 'binary_sensor',          'ºC',          0x0010           ],
  'shuntn'             : ['r10', 'binary_sensor',          'ºC',          0x0020           ],
  'shuntp'             : ['r10', 'binary_sensor',          'ºC',          0x0040           ],
  'ts1'                : ['r10', 'binary_sensor',          'ºC',          0x0080           ],
  'shntgrpn'           : ['r11', 'binary_sensor',          'ºC',          0x0001           ],
  'shntgrpp'           : ['r11', 'binary_sensor',          'ºC',          0x0002           ],
  'shnt_kyln'          : ['r11', 'binary_sensor',          'ºC',          0x0004           ],
  'shnt_kylp'          : ['r11', 'binary_sensor',          'ºC',          0x0008           ],
  'akt_kyl'            : ['r11', 'binary_sensor',          'ºC',          0x0010           ],
  'pass_kyl'           : ['r11', 'binary_sensor',          'ºC',          0x0020           ],
  'larm'               : ['r11', 'binary_sensor',          'ºC',          0x0040           ],
  'pwm_ut'             : ['r12', 'sensor',                 '%',                             ],
  'alm_hp'             : ['r13', 'binary_sensor',          '%',            0x0001           ],
  'alm_lp'             : ['r13', 'binary_sensor',          '%',            0x0002           ],
  'alm_ms'             : ['r13', 'binary_sensor',          '%',            0x0004           ],
  'alm_blf'            : ['r13', 'binary_sensor',          '%',            0x0008           ],
  'alm_blt'            : ['r13', 'binary_sensor',          '%',            0x0010           ],
  'alm_ute'            : ['r14', 'binary_sensor',          '%',            0x0001           ],
  'alm_fram'           : ['r14', 'binary_sensor',          '%',            0x0002           ],
  'alm_retur'          : ['r14', 'binary_sensor',          '%',            0x0004           ],
  'alm_vv'             : ['r14', 'binary_sensor',          '%',            0x0008           ],
  'alm_rum'            : ['r14', 'binary_sensor',          '%',            0x0010           ],
  'alm_fas'            : ['r14', 'binary_sensor',          '%',            0x0020           ],
  'alm_ovrh'           : ['r14', 'binary_sensor',          '%',            0x0040           ],
  'behov1'             : ['r15', 'sensor',                 '',                              ],
  'behov2'             : ['r16', 'sensor',                 '',                              ],
  'tryckr_t'           : ['r17', 'temperature',            'ºC',                           ],
  'hgw_vv'             : ['r18', 'temperature',            'ºC',                           ],
  'integr'             : ['r19', 'sensor',                 'Cmin',                          ],
  'intgr_steg'         : ['r1a', 'sensor',                 '',                              ],
  'clk_vv'             : ['r1b', 'time',                   '10s',                           ],
  'min_time_start'     : ['r1c', 'time',                   'min',                           ],
  'sw_ver'             : ['r1d', 'sensor',                 '',                              ],
  'cirk_speed'         : ['r1e', 'sensor',                 '%',                             ],
  'brine_speed'        : ['r1f', 'sensor',                 '%',                             ],
  'clk_vv_stop'        : ['r20', 'sensor',                 '',                              ],
  'rum_bor2'           : ['r32', 'temperature_input',      'ºC',               0,     50   ],
  'dl'                 : ['r33', 'select_input',           'mode',              0,     16   ],
  'kurva'              : ['r34', 'sensor_input',           '',                  0,    200   ],
  'kurva_min'          : ['r35', 'sensor_input',           '',                  0,    200   ],
  'kurva_max'          : ['r36', 'sensor_input',           '',                  0,    200   ],
  'kurva_p5'           : ['r37', 'sensor_input',           '',                  0,    200   ],
  'kurva_0'            : ['r38', 'sensor_input',           '',                  0,    200   ],
  'kurva_n5'           : ['r39', 'sensor_input',           '',                  0,    200   ],
  'varme_stp'          : ['r3a', 'temperature_input',      'ºC',               0,    200   ],
  'sankn_t'            : ['r3b', 'temperature_input',      'ºC',               0,    100   ],
  'rumfakt'            : ['r3c', 'sensor_input',           '',                  0,      2   ],
  'kurva2'             : ['r3d', 'sensor_input',           '',                  0,    200   ],
  'kurva2_min'         : ['r3e', 'sensor_input',           '',                  0,    200   ],
  'kurva2_max'         : ['r3f', 'sensor_input',           '',                  0,    200   ],
  'kurva2_bor'         : ['r40', 'temperature_input',      'ºC',               0,    200   ],
  'kurva2_ar'          : ['r41', 'temperature_input',      'ºC',               0,    200   ],
  'status6'            : ['r42', 'sensor_input',           '',             -32768,  32767   ],
  'tryckr_limit'       : ['r43', 'temperature_input',      'ºC',               0,    200   ],
  'vv_start'           : ['r44', 'temperature_input',      'ºC',               0,    100   ],
  'vv_tid'             : ['r45', 'time_input',             'min',               0,  32767   ],
  'varme_tid'          : ['r46', 'time_input',             'min',               0,  32767   ],
  'leg_interv'         : ['r47', 'time_input',             'days',              0,  32767   ],
  'leg_stop_t'         : ['r48', 'temperature_input',      'ºC',               0,    100   ],
  'integr_a1'          : ['r49', 'sensor_input',           'Cmin',         -32768,  32767   ],
  'hyst_vp'            : ['r4a', 'temperature_input',      'ºC',               0,    100   ],
  'max_ret'            : ['r4b', 'temperature_input',      'ºC',               0,    100   ],
  'min_st_int'         : ['r4c', 'time_input',             'min',               0,  32767   ],
  'min_brine_t'        : ['r4d', 'temperature_input',      'ºC',             -25,    100   ],
  'kyla_bor'           : ['r4e', 'temperature_input',      'ºC',               0,     50   ],
  'integr_a2'          : ['r4f', 'sensor_input',           '10Cmin',            0,    200   ],
  'hyst_ts'            : ['r50', 'temperature_input',      'ºC',               0,    100   ],
  'max_steg_ts'        : ['r51', 'sensor_input',           'steps',        -32768,  32767   ],
  'max_strom'          : ['r52', 'sensor_input',           'A',            -32768,  32767   ],
  'shunttid'           : ['r53', 'time_input',             's',                 0,  32767   ],
  'vv_stop'            : ['r54', 'temperature_input',      'ºC',               0,    100   ],
  'test_mode'          : ['r55', 'sensor',                 'mode',                          ],
  'status7'            : ['r56', 'sensor',                 '',                              ],
  'lang'               : ['r57', 'sensor_language',        'language',                      ],
  'status8'            : ['r58', 'sensor',                 '',                              ],
  'fabriksinst'        : ['r59', 'sensor',                 'setting',                       ],
  'reset_dr_tid'       : ['r5a', 'sensor_boolean',         'Boolean',                       ],
  'cal_ute'            : ['r5b', 'temperature',            'ºC',                           ],
  'cal_fram'           : ['r5c', 'temperature',            'ºC',                           ],
  'cal_ret'            : ['r5d', 'temperature',            'ºC',                           ],
  'cal_vv'             : ['r5e', 'temperature',            'ºC',                           ],
  'cal_brut'           : ['r5f', 'temperature',            'ºC',                           ],
  'cal_brin'           : ['r60', 'temperature',            'ºC',                           ],
  'sys_typ'            : ['r61', 'sensor',                 'type',                          ],
  'till_fasm'          : ['r62', 'binary_sensor',          'type',         0x0001           ],
  'till_2'             : ['r62', 'binary_sensor',          'type',         0x0002           ],
  'till_hgw'           : ['r62', 'binary_sensor',          'type',         0x0004           ],
  'till_4'             : ['r62', 'binary_sensor',          'type',         0x0008           ],
  'till_5'             : ['r62', 'binary_sensor',          'type',         0x0010           ],
  'till_6'             : ['r62', 'binary_sensor',          'type',         0x0020           ],
  'till_opt'           : ['r62', 'binary_sensor',          'type',         0x0040           ],
  'till_fw'            : ['r62', 'binary_sensor',          'type',         0x0080           ],
  'log_tim'            : ['r63', 'time',                   'min',                           ],
  'brine_tim_on'       : ['r64', 'time',                   '10s',                           ],
  'brine_tim_off'      : ['r65', 'time',                   '10s',                           ],
  'leg_top_on'         : ['r66', 'sensor_boolean',         'Boolean',                       ],
  'leg_top_tim'        : ['r67', 'time',                   'h',                             ],
  'dr_tim_vp'          : ['r68', 'time',                   'h',                             ],
  'status10'           : ['r69', 'sensor',                 '',                              ],
  'dr_tim_ts1'         : ['r6a', 'time',                   'h',                             ],
  'status11'           : ['r6b', 'sensor',                 '',                              ],
  'dr_tim_vv'          : ['r6c', 'time',                   'h',                             ],
  'status12'           : ['r6d', 'sensor',                 '',                              ],
  'dr_tim_pas_kyl'     : ['r6e', 'time',                   'h',                             ],
  'status13'           : ['r6f', 'sensor',                 '',                              ],
  'dr_tim_akt_kyl'     : ['r70', 'time',                   'h',                             ],
  'status14'           : ['r71', 'sensor',                 '',                              ],
  'dr_tim_ts2'         : ['r72', 'time',                   'h',                             ],
  'status15'           : ['r73', 'sensor',                 '',                              ],
  'status16'           : ['r74', 'sensor',                 '',                              ],
  'sensor_meassured'   : ['rf0', 'temperature',            'ºC',               0,     50   ],

}

# Translation dictionary
id_names = {  
  't_ute'              : 'Outdoor temp.',
  't_rum_ar'           : 'Indoor temp.',
  't_rum_ar_dec'       : 'Indoor temp., decimal',
  't_rum_bor'          : 'Indoor target temp.',
  't_rum_bor_dec'      : 'Indoor target temp., decimal',
  't_fram'             : 'Supplyline temp.',
  't_retur'            : 'Returnline temp.',
  't_vatten'           : 'Hotwater temp.',
  't_brine_ut'         : 'Brine out temp.',
  't_brine_in'         : 'Brine in temp.',
  't_kylning'          : 'Cooling temp.',
  't_fram_shunt'       : 'Supplyline temp., shunt',
  'stromforbr'         : 'Electrical Current',
  'ts_1'               : 'Aux. heater 3 kW',
  'ts_2'               : 'Aux. heater 6 kW',
  't_fram_bor'         : 'Supplyline target temp.',
  't_fram_shunt_bor'   : 'Supplyline target temp., shunt',
  'brine'              : 'Brinepump',
  'kompr'              : 'Compressor',
  'cirkp'              : 'Flowlinepump',
  'varmvatten'         : 'Hotwater production.',
  'ts2'                : 'Auxilliary 2',
  'shuntn'             : 'Shunt -',
  'shuntp'             : 'Shunt +',
  'ts1'                : 'Auxilliary 1',
  'shntgrpn'           : 'Shuntgroup -',
  'shntgrpp'           : 'Shuntgroup +',
  'shnt_kyln'          : 'Shunt cooling -',
  'shnt_kylp'          : 'Shunt cooling +',
  'akt_kyl'            : 'Active cooling',
  'pass_kyl'           : 'Passive cooling',
  'larm'               : 'Alarm',
  'pwm_ut'             : 'PWM Out',
  'alm_hp'             : 'Alarm highpr.pressostate',
  'alm_lp'             : 'Alarm lowpr.pressostate',
  'alm_ms'             : 'Alarm motorcircuit breaker',
  'alm_blf'            : 'Alarm low flow brine',
  'alm_blt'            : 'Alarm low temp. brine',
  'alm_ute'            : 'Alarm outdoor t-sensor',
  'alm_fram'           : 'Alarm supplyline t-sensor',
  'alm_retur'          : 'Alarm returnline t-sensor',
  'alm_vv'             : 'Alarm hotw. t-sensor',
  'alm_rum'            : 'Alarm indoor t-sensor',
  'alm_fas'            : 'Alarm incorrect 3-phase order',
  'alm_ovrh'           : 'Alarm overheating',
  'behov1'             : 'DEMAND1',
  'behov2'             : 'DEMAND2',
  'tryckr_t'           : 'Pressurepipe temp.',
  'hgw_vv'             : 'Hotw. supplyline temp.',
  'integr'             : 'Integral',
  'intgr_steg'         : 'Integral, reached A-limit',
  'clk_vv'             : 'Defrost',
  'min_time_start'     : 'Minimum time to start',
  'sw_ver'             : 'Program version',
  'cirk_speed'         : 'Flowlinepump speed',
  'brine_speed'        : 'Brinepump speed',
  'clk_vv_stop'        : 'STATUS3',
  'rum_bor2'           : 'Indoor target temp.',
  'dl'                 : 'Mode',
  'kurva'              : 'Curve',
  'kurva_min'          : 'Curve min',
  'kurva_max'          : 'Curve max',
  'kurva_p5'           : 'Curve +5',
  'kurva_0'            : 'Curve 0',
  'kurva_n5'           : 'Curve -5',
  'varme_stp'          : 'Heatstop',
  'sankn_t'            : 'Temp. reduction',
  'rumfakt'            : 'Room factor',
  'kurva2'             : 'Curve 2',
  'kurva2_min'         : 'Curve 2 min',
  'kurva2_max'         : 'Curve 2 max',
  'kurva2_bor'         : 'Curve 2, Target',
  'kurva2_ar'          : 'Curve 2, Actual',
  'status6'            : 'Outdoor stop temp. (20=-20C)',
  'tryckr_limit'       : 'Pressurepipe, temp. limit',
  'vv_start'           : 'Hotwater starttemp.',
  'vv_tid'             : 'Hotwater operating time',
  'varme_tid'          : 'Heatpump operating time',
  'leg_interv'         : 'Legionella interval',
  'leg_stop_t'         : 'Legionella stop temp.',
  'integr_a1'          : 'Integral limit A1',
  'hyst_vp'            : 'Hysteresis, heatpump',
  'max_ret'            : 'Returnline temp., max limit',
  'min_st_int'         : 'Minimum starting interval',
  'min_brine_t'        : 'Brinetemp., min limit (-15=OFFV)',
  'kyla_bor'           : 'Cooling, target',
  'integr_a2'          : 'Integral limit A2',
  'hyst_ts'            : 'Hysteresis limit, aux',
  'max_steg_ts'        : 'Max step, aux',
  'max_strom'          : 'Electrical current, max limit',
  'shunttid'           : 'Shunt time',
  'vv_stop'            : 'Hotwater stop temp.',
  'test_mode'          : 'Manual test mode',
  'status7'            : 'DT_LARMOFF',
  'lang'               : 'Language',
  'status8'            : 'SERVFAS',
  'fabriksinst'        : 'Factory settings',
  'reset_dr_tid'       : 'Reset runtime counters',
  'cal_ute'            : 'Calibration outdoor sensor',
  'cal_fram'           : 'Calibration supplyline sensor',
  'cal_ret'            : 'Calibration returnline sensor',
  'cal_vv'             : 'Calibration hotwater sensor',
  'cal_brut'           : 'Calibration brine out sensor',
  'cal_brin'           : 'Calibration brine in sensor',
  'sys_typ'            : 'Heating system type 0=VL 4=D',
  'till_fasm'          : 'Add-on phase order measurement',
  'till_2'             : 'TILL2',
  'till_hgw'           : 'Add-on HGW',
  'till_4'             : 'TILL4',
  'till_5'             : 'TILL5',
  'till_6'             : 'TILL6',
  'till_opt'           : 'Add-on Optimum',
  'till_fw'            : 'Add-on flow guard',
  'log_tim'            : 'Logging time',
  'brine_tim_on'       : 'Brine run-out duration',
  'brine_tim_off'      : 'Brine run-in duration',
  'leg_top_on'         : 'Legionella peak heating enable',
  'leg_top_tim'        : 'Legionella peak heating duration',
  'dr_tim_vp'          : 'Runtime compressor',
  'status10'           : 'DVP_MSD1',
  'dr_tim_ts1'         : 'Runtime 3 kW',
  'status11'           : 'DTS_MSD1',
  'dr_tim_vv'          : 'Runtime hotwater production',
  'status12'           : 'DVV_MSD1',
  'dr_tim_pas_kyl'     : 'Runtime passive cooling',
  'status13'           : 'DPAS_MSD1',
  'dr_tim_akt_kyl'     : 'Runtime active cooling',
  'status14'           : 'DACT_MSD1',
  'dr_tim_ts2'         : 'Runtime 6 kW',
  'status15'           : 'DTS2_MSD1',
  'status16'           : 'GrafCounterOffSet',


}
# Unit dictionary
id_units = {  
  't_ute'              : 'ºC',
  't_rum_ar'           : 'ºC',
  't_rum_ar_dec'       : '0.1C',
  't_rum_bor'          : 'ºC',
  't_rum_bor_dec'      : '0.1C',
  't_fram'             : 'ºC',
  't_retur'            : 'ºC',
  't_vatten'           : 'ºC',
  't_brine_ut'         : 'ºC',
  't_brine_in'         : 'ºC',
  't_kylning'          : 'ºC',
  't_fram_shunt'       : 'ºC',
  'stromforbr'         : 'A',
  'ts_1'               : 'Boolean',
  'ts_2'               : 'Boolean',
  't_fram_bor'         : 'ºC',
  't_fram_shunt_bor'   : 'ºC',
  'brine'              : 'Boolean',
  'kompr'              : 'Boolean',
  'cirkp'              : 'Boolean',
  'varmvatten'         : 'Boolean',
  'ts2'                : 'Boolean',
  'shuntn'             : 'Boolean',
  'shuntp'             : 'Boolean',
  'ts1'                : 'Boolean',
  'shntgrpn'           : 'Boolean',
  'shntgrpp'           : 'Boolean',
  'shnt_kyln'          : 'Boolean',
  'shnt_kylp'          : 'Boolean',
  'akt_kyl'            : 'Boolean',
  'pass_kyl'           : 'Boolean',
  'larm'               : 'Boolean',
  'pwm_ut'             : '%',
  'alm_hp'             : 'Boolean',
  'alm_lp'             : 'Boolean',
  'alm_ms'             : 'Boolean',
  'alm_blf'            : 'Boolean',
  'alm_blt'            : 'Boolean',
  'alm_ute'            : 'Boolean',
  'alm_fram'           : 'Boolean',
  'alm_retur'          : 'Boolean',
  'alm_vv'             : 'Boolean',
  'alm_rum'            : 'Boolean',
  'alm_fas'            : 'Boolean',
  'alm_ovrh'           : 'Boolean',
  'behov1'             : '  ',
  'behov2'             : '  ',
  'tryckr_t'           : 'ºC',
  'hgw_vv'             : 'ºC',
  'integr'             : 'C*min',
  'intgr_steg'         : '  ',
  'clk_vv'             : '*10s',
  'min_time_start'     : 'min',
  'sw_ver'             : '  ',
  'cirk_speed'         : '%',
  'brine_speed'        : '%',
  'clk_vv_stop'        : '  ',
  'rum_bor2'           : 'ºC',
  'dl'                 : 'läge #',
  'kurva'              : '*',
  'kurva_min'          : '*',
  'kurva_max'          : '*',
  'kurva_p5'           : '*',
  'kurva_0'            : '*',
  'kurva_n5'           : '*',
  'varme_stp'          : 'ºC',
  'sankn_t'            : 'ºC',
  'rumfakt'            : '*',
  'kurva2'             : '*',
  'kurva2_min'         : '*',
  'kurva2_max'         : '*',
  'kurva2_bor'         : 'ºC',
  'kurva2_ar'          : 'ºC',
  'status6'            : '*',
  'tryckr_limit'       : 'ºC',
  'vv_start'           : 'ºC',
  'vv_tid'             : 'min',
  'varme_tid'          : 'min',
  'leg_interv'         : 'days',
  'leg_stop_t'         : 'ºC',
  'integr_a1'          : 'C*min',
  'hyst_vp'            : 'ºC',
  'max_ret'            : 'ºC',
  'min_st_int'         : 'min',
  'min_brine_t'        : 'ºC',
  'kyla_bor'           : 'ºC',
  'integr_a2'          : '10C*min',
  'hyst_ts'            : 'ºC',
  'max_steg_ts'        : '# steps',
  'max_strom'          : 'A',
  'shunttid'           : 's',
  'vv_stop'            : 'ºC',
  'test_mode'          : 'mode #',
  'status7'            : '  ',
  'lang'               : 'language #',
  'status8'            : '  ',
  'fabriksinst'        : 'setting #',
  'reset_dr_tid'       : 'Boolean',
  'cal_ute'            : 'ºC',
  'cal_fram'           : 'ºC',
  'cal_ret'            : 'ºC',
  'cal_vv'             : 'ºC',
  'cal_brut'           : 'ºC',
  'cal_brin'           : 'ºC',
  'sys_typ'            : 'type #',
  'till_fasm'          : 'Boolean',
  'till_2'             : 'Boolean',
  'till_hgw'           : 'Boolean',
  'till_4'             : 'Boolean',
  'till_5'             : 'Boolean',
  'till_6'             : 'Boolean',
  'till_opt'           : 'Boolean',
  'till_fw'            : 'Boolean',
  'log_tim'            : 'min',
  'brine_tim_on'       : '*10s',
  'brine_tim_off'      : '*10s',
  'leg_top_on'         : 'Boolean',
  'leg_top_tim'        : 'h',
  'dr_tim_vp'          : 'h',
  'status10'           : '  ',
  'dr_tim_ts1'         : 'h',
  'status11'           : '  ',
  'dr_tim_vv'          : 'h',
  'status12'           : '  ',
  'dr_tim_pas_kyl'     : 'h',
  'status13'           : '  ',
  'dr_tim_akt_kyl'     : 'h',
  'status14'           : '  ',
  'dr_tim_ts2'         : 'h',
  'status15'           : '  ',
  'status16'           : '  ',
  'sensor_meassured'   : 'ºC',

}
