#!/usr/bin/env python

# TODO
# hashbang
# rename
# viz: generic 1 and 2 qubit gates
# Generic multiqubit gates?

from sympy import Symbol

import quantumflow as qf

t = Symbol('t')
theta = Symbol('theta')
theta0 = Symbol('theta_0')
theta1 = Symbol('theta_1')
theta2 = Symbol('theta_2')
phi = Symbol('phi')
alpha = Symbol('alpha')
tx = Symbol("t_x")
ty = Symbol("t_y")
tz = Symbol("t_z")
sx = Symbol("s_x")
sy = Symbol("s_y")
sz = Symbol("s_z")


q0, q1, q2, q3, q4, q5, q6, q7, q8 = 0, 1, 2, 3, 4, 5, 6, 7, 8


def write_latex(fname, circ, left_labels=None, right_labels=None):
    # scale = 0.75
    latex = qf.circuit_to_latex(circ, document=False, package='quantikz',
                                qubit_labels=False, scale=0.8,
                                left_labels=left_labels, right_labels=right_labels)
    with open(fname + '.tex', "w") as fout:
        fout.write(latex)

    print('.', end='')


fname = 'CCNot_labels'
gate = qf.CCNot(q0, q1, q2)
circ = qf.Circuit(gate)
write_latex(fname, circ, ["A", "B", "T"], ["A", "B", "T+AB"])


fname = 'CCCNot'
gate = qf.ControlledGate(qf.X(q3), [q0, q1, q2])
circ = qf.Circuit(gate)
write_latex(fname, circ)


fname = 'C7Not_labels'
gate = qf.ControlledGate(qf.X(q7), [q0, q1, q2, q3, q4, q5, q6])
circ = qf.Circuit([gate])
write_latex(fname, circ, ["A",'B','C','D','E','F','G','T'], ["A",'B','C','D','E','F','G','T+ABCDEFG'] )


fname = 'C7Not_labels_1'
circ = qf.Circuit([qf.ControlledGate(qf.X(q7), [q0, q2, q4, q6]),
  qf.ControlledGate(qf.X(q8), [q1, q3, q5, q7]),
  qf.ControlledGate(qf.X(q7), [q0, q2, q4, q6]),
   qf.ControlledGate(qf.X(q8), [q1, q3, q5, q7]),
  ])
write_latex(fname, circ, ["A",'B','C','D','E','F','G','b', 'T'], ["A",'B','C','D','E','F','G', 'b', 'T+ABCDEFG'] )


fname = 'peres_halfadder'
circ = qf.Circuit([qf.CCNot(0, 1, 2), qf.CNot(0, 1)])
write_latex(fname, circ, ["A", "B", "0"], ["A", "Sum", "Carry"])



print()