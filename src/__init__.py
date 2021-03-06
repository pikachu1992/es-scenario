#!/usr/bin/env python3

_LPPR_SETTINGS = {
  '35': 'ILS35:N041.13.59,934:W008.40.38,582:352',
  '17': None,
  'ALL': [
    'AIRPORT_ALT:0'
  ],
  'DEPARTURE_CALLSIGNS': {
    'LPPT': ['SWT230P', 'RYR2093', 'RYR2095', 'RYR2695', 'TAP1921', 'TAP1923', 'TAP1925',],
    'LPFR': ['RYR5486',],
    'LPMA': ['TVF93AF', 'TVF72BN', 'TAP1711', 'TAP1713', 'EZY7585']
  },
  'DEPARTURE_FPL': {
    # all lines start with $FP{callsign}
    'LPPT': [
      ':*A:I:B738:400:LPPR:0000:0000:190:LPPT:00:00:0:0::/v/:MANIK DCT XAMAX',
      ':*A:I:B738:410:LPPR:0000:0000:210:LPPT:00:00:0:0::/v/:MANIK DCT XAMAX',
      ':*A:I:B738:420:LPPR:0000:0000:230:LPPT:00:00:0:0::/v/:MANIK DCT XAMAX',
    ],
    'LPFR': [
      ':*A:I:B738:410:LPPR:0000:0000:210:LPFR:00:00:0:0::/v/:MANIK DCT INBOM DCT ALAGU',
      ':*A:I:B738:420:LPPR:0000:0000:230:LPFR:00:00:0:0::/v/:MANIK DCT INBOM DCT ALAGU',
      ':*A:I:B738:430:LPPR:0000:0000:250:LPFR:00:00:0:0::/v/:MANIK DCT INBOM DCT ALAGU',
    ],
    'LPMA': [
      ':*A:I:B738:440:LPPR:0000:0000:350:LPMA:00:00:0:0::/v/:MANIK LAMDI VERAM LIDRO',
      ':*A:I:B738:450:LPPR:0000:0000:370:LPMA:00:00:0:0::/v/:MANIK LAMDI VERAM LIDRO',
      ':*A:I:B738:460:LPPR:0000:0000:390:LPMA:00:00:0:0::/v/:MANIK LAMDI VERAM LIDRO',
    ]
  },
  'STANDS': [
    '41.235106:-8.672932',
    '41.236885:-8.672543',
    '41.237945:-8.673614',
    '41.236422:-8.672466',
    '41.237352:-8.672720',
    '41.235355:-8.674780',
    '41.238571:-8.675655',
    '41.235074:-8.672887',
    '41.237786:-8.672925',
    '41.234497:-8.672475',
    '41.235571:-8.672493',
  ]
}

AIRPORT_SETTINGS = {
  'LPPR': _LPPR_SETTINGS,
}