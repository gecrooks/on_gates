#!/usr/bin/env python

# TODO
# hashbang
# rename
# viz: generic 1 and 2 qubit gates
# Generic multiqubit gates?

from sympy import Symbol

import quantumflow as qf


def write_latex(fname, circ):
    # scale = 0.75
    latex = qf.circuit_to_latex(circ, document=False, package='quantikz',
                                qubit_labels=False)
    with open(fname + '.tex', "w") as fout:
        fout.write(latex)

    print('.', end='')


fname = 'cnot'
circ = qf.Circuit([qf.CNot(0, 1)])
write_latex(fname, circ)

fname = 'cnot_switch'
circ = qf.Circuit([qf.H(0), qf.H(1), qf.CNot(1, 0), qf.H(0), qf.H(1)])
# assert equaltiy
write_latex(fname, circ)

fname = 'swap'
circ = qf.Circuit([qf.Swap(0, 1)])
write_latex(fname, circ)

fname = 'swap_to_cnot'
circ = qf.Circuit([qf.CNot(0, 1), qf.CNot(1, 0), qf.CNot(0, 1)])
write_latex(fname, circ)

fname = 'dcnot'
circ = qf.Circuit([qf.CNot(0, 1), qf.CNot(1, 0)])
write_latex(fname, circ)

fname = 'iswap_to_dcnot'
circ = qf.Circuit([qf.H(0), qf.S_H(0), qf.S_H(1), qf.ISwap(1, 0), qf.H(1)])
write_latex(fname, circ)

# FIXME
# fname = 'magic'
# circ = qf.Circuit([qf.Unitary(name='M', qubits=[0, 1], tensor=qf.I(0, 1).tensor)])
# write_latex(fname, circ)

fname = 'magic_circ'
circ = qf.Circuit([qf.S(0), qf.S(1), qf.H(1), qf.CNot(1, 0)])
write_latex(fname, circ)

# fname = 'qft'
# circ = qf.Circuit([qf.Unitary(qf.IDEN(0, 1).tensor, 0, 1, name='QFT')])
# write_latex(fname, circ)

fname = 'qft_circ'
circ = qf.Circuit([qf.Swap(0, 1), qf.H(1), qf.CZ(0, 1), qf.H(0)])
write_latex(fname, circ)

fname = 'cz'
circ = qf.Circuit([qf.CZ(0, 1)])
write_latex(fname, circ)

fname = 'cv'
circ = qf.Circuit([qf.CV(0, 1)])
write_latex(fname, circ)

fname = 'cv_to_cpt'
circ = qf.Circuit(qf.translate_cv_to_cpt(qf.CV(0, 1)))
write_latex(fname, circ)

fname = 'cv2'
circ = qf.Circuit([qf.CV(0, 1), qf.CV(0, 1)])
write_latex(fname, circ)

fname = 'cnot_to_cz'
circ = qf.Circuit([qf.H(1), qf.CNot(0, 1), qf.H(1)])
write_latex(fname, circ)

fname = 'ccnot'
circ = qf.Circuit([qf.CCNot(0, 1, 2)])
write_latex(fname, circ)

fname = 'cswap'
circ = qf.Circuit([qf.CSwap(0, 1, 2)])
write_latex(fname, circ)

fname = 'I'
circ = qf.Circuit([qf.I(0)])
write_latex(fname, circ)

fname = 'X'
circ = qf.Circuit([qf.X(0)])
write_latex(fname, circ)

fname = 'Y'
circ = qf.Circuit([qf.Y(0)])
write_latex(fname, circ)

fname = 'Z'
circ = qf.Circuit([qf.Z(0)])
write_latex(fname, circ)

fname = 'S'
circ = qf.Circuit([qf.S(0)])
write_latex(fname, circ)

fname = 'S_H'
circ = qf.Circuit([qf.S_H(0)])
write_latex(fname, circ)


fname = 'V'
circ = qf.Circuit([qf.V(0)])
write_latex(fname, circ)

fname = 'V_H'
circ = qf.Circuit([qf.V_H(0)])
write_latex(fname, circ)

# fname = 'SqrtY'
# circ = qf.Circuit([qf.YPow(0.5, 0)])
# write_latex(fname, circ)

# fname = 'SqrtY_H'
# circ = qf.Circuit([qf.YPow(-0.5, 0)])
# write_latex(fname, circ)


fname = 'SqrtX'
circ = qf.Circuit([qf.XPow(1/2, 0)])
write_latex(fname, circ)

fname = 'SqrtX_H'
circ = qf.Circuit([qf.XPow(-1/2, 0)])
write_latex(fname, circ)


fname = 'SqrtY'
circ = qf.Circuit([qf.SqrtY(0)])
write_latex(fname, circ)

fname = 'SqrtY_H'
circ = qf.Circuit([qf.SqrtY_H(0)])
write_latex(fname, circ)


fname = 'SqrtZ'
circ = qf.Circuit([qf.ZPow(1/2, 0)])
write_latex(fname, circ)

fname = 'SqrtZ_H'
circ = qf.Circuit([qf.ZPow(-1/2, 0)])
write_latex(fname, circ)


fname = 'T'
circ = qf.Circuit([qf.T(0)])
write_latex(fname, circ)

fname = 'T_H'
circ = qf.Circuit([qf.T_H(0)])
write_latex(fname, circ)

fname = 'H'
circ = qf.Circuit([qf.H(0)])
write_latex(fname, circ)

fname = "H_ZY"
circ0 = qf.Circuit([qf.Z(0), qf.Y(0)**0.5])
assert qf.gates_close(circ.asgate(), circ0.asgate())
write_latex(fname, circ0)

fname = "H_SVS"
circ0 = qf.Circuit([qf.S(0), qf.V(0), qf.S(0)])
assert qf.gates_close(circ.asgate(), circ0.asgate())
write_latex(fname, circ0)


fname = 'xx'
circ = qf.Circuit([qf.XX(Symbol('t'), 0, 1, )])
write_latex(fname, circ)

fname = 'yy'
circ = qf.Circuit([qf.YY(Symbol('t'), 0, 1, )])
write_latex(fname, circ)

fname = 'zz'
circ = qf.Circuit([qf.ZZ(Symbol('t'), 0, 1, )])
write_latex(fname, circ)

fname = 'RX'
circ = qf.Circuit([qf.Rx(Symbol(r'\theta'), 0)])
write_latex(fname, circ)

fname = 'RX0_RX_1'
circ = qf.Circuit([qf.Rx(Symbol(r'\theta_0'), 0), qf.Rx(Symbol(r'\theta_1'), 0)])
write_latex(fname, circ)

fname = 'RX01'
circ = qf.Circuit(qf.Rx(Symbol(r'\theta_0+\theta_1'), 0))
write_latex(fname, circ)


fname = 'RY0_RY_1'
circ = qf.Circuit([qf.Ry(Symbol(r'\theta_0'), 0), qf.Ry(Symbol(r'\theta_1'), 0)])
write_latex(fname, circ)

fname = 'RY01'
circ = qf.Circuit(qf.Ry(Symbol(r'\theta_0+\theta_1'), 0))
write_latex(fname, circ)


fname = 'RZ0_RZ_1'
circ = qf.Circuit([qf.Rz(Symbol(r'\theta_0'), 0), qf.Rz(Symbol(r'\theta_1'), 0)])
write_latex(fname, circ)

fname = 'RZ01'
circ = qf.Circuit(qf.Rz(Symbol(r'\theta_0+\theta_1'), 0))
write_latex(fname, circ)


fname = 'RY'
circ = qf.Circuit([qf.Ry(Symbol(r'\theta'), 0)])
write_latex(fname, circ)

fname = 'RZ'
circ = qf.Circuit([qf.Rz(Symbol(r'\theta'), 0)])
write_latex(fname, circ)

fname = 'XPow'
circ = qf.Circuit([qf.XPow(Symbol('t'), 0)])
write_latex(fname, circ)

fname = 'YPow'
circ = qf.Circuit([qf.YPow(Symbol('t'), 0)])
write_latex(fname, circ)

fname = 'ZPow'
circ = qf.Circuit([qf.ZPow(Symbol('t'), 0)])
write_latex(fname, circ)

# FIXME
# fname = 'ph'
# circ = qf.Circuit([qf.Unitary(name='h', qubits=[0], tensor=qf.I(0).tensor)])
# write_latex(fname, circ)

# FIXME
# fname = 'inv_ph'
# circ = qf.Circuit([qf.Unitary(name=Symbol(r'h$^\dagger$'),
#                            qubits=[0], tensor=qf.I(0).tensor)])
# write_latex(fname, circ)

fname = 'ecp'
circ = qf.Circuit([qf.ECP(0, 1)])
write_latex(fname, circ)

fname = 'ecp_to_sqrtiswap'
circ = qf.Circuit(qf.translate_ecp_to_sqrtiswap(qf.ECP(0, 1)))
write_latex(fname, circ)

fname = 'w_to_ecp'
circ = qf.Circuit(qf.translate_w_to_ecp(qf.W(0, 1)))
write_latex(fname, circ)

fname = 'w_to_ch_cnot'
circ = qf.Circuit(qf.translate_w_to_ch_cnot(qf.W(0, 1)))
write_latex(fname, circ)

fname = 'w_to_cnot'
circ = qf.Circuit(qf.translate_w_to_cnot(qf.W(0, 1)))
write_latex(fname, circ)


fname = 'peres'
circ = qf.Circuit([qf.CCNot(0, 1, 2), qf.CNot(0, 1)])
write_latex(fname, circ)

deutsch = qf.Deutsch(Symbol(r'\theta'), 0, 1, 2)
fname = 'deutsch'
circ = qf.Circuit(deutsch)
write_latex(fname, circ)

fname = 'deutsch_to_barenco'
circ = qf.Circuit(qf.translate_deutsch_to_barenco(deutsch))
write_latex(fname, circ)


# Clifford transforms

fname = 'clifford_cz_x0'
circ0 = qf.Circuit([qf.CZ(0, 1).H, qf.X(0), qf.CZ(0, 1)])
circ1 = qf.Circuit([qf.X(0), qf.Z(1)])
assert qf.gates_phase_close(circ0.asgate(), circ1.asgate())
write_latex(fname, circ0)
write_latex(fname+'_res', circ1)

fname = 'clifford_cz_x1'
circ0 = qf.Circuit([qf.CZ(0, 1).H, qf.X(1), qf.CZ(0, 1)])
circ1 = qf.Circuit([qf.Z(0), qf.X(1)])
assert qf.gates_phase_close(circ0.asgate(), circ1.asgate())
write_latex(fname, circ0)
write_latex(fname+'_res', circ1)

fname = 'clifford_cz_z0'
circ0 = qf.Circuit([qf.CZ(0, 1).H, qf.Z(0), qf.CZ(0, 1)])
circ1 = qf.Circuit([qf.Z(0), qf.I(1)])
assert qf.gates_phase_close(circ0.asgate(), circ1.asgate())
write_latex(fname, circ0)
write_latex(fname+'_res', circ1)

fname = 'clifford_cz_z1'
circ0 = qf.Circuit([qf.CZ(0, 1).H, qf.Z(1), qf.CZ(0, 1)])
circ1 = qf.Circuit([qf.I(0), qf.Z(1)])
assert qf.gates_phase_close(circ0.asgate(), circ1.asgate())
write_latex(fname, circ0)
write_latex(fname+'_res', circ1)


fname = 'clifford_cnot_x0'
circ0 = qf.Circuit([qf.CNot(0, 1).H, qf.X(0), qf.CNot(0, 1)])
circ1 = qf.Circuit([qf.X(0), qf.X(1)])
assert qf.gates_phase_close(circ0.asgate(), circ1.asgate())
write_latex(fname, circ0)
write_latex(fname+'_res', circ1)

fname = 'clifford_cnot_x1'
circ0 = qf.Circuit([qf.CNot(0, 1).H, qf.X(1), qf.CNot(0, 1)])
circ1 = qf.Circuit([qf.I(0), qf.X(1)])
assert qf.gates_phase_close(circ0.asgate(), circ1.asgate())
write_latex(fname, circ0)
write_latex(fname+'_res', circ1)

fname = 'clifford_cnot_z0'
circ0 = qf.Circuit([qf.CNot(0, 1).H, qf.Z(0), qf.CNot(0, 1)])
circ1 = qf.Circuit([qf.Z(0), qf.I(1)])
assert qf.gates_phase_close(circ0.asgate(), circ1.asgate())
write_latex(fname, circ0)
write_latex(fname+'_res', circ1)

fname = 'clifford_cnot_z1'
circ0 = qf.Circuit([qf.CNot(0, 1).H, qf.Z(1), qf.CNot(0, 1)])
circ1 = qf.Circuit([qf.Z(0), qf.Z(1)])
assert qf.gates_phase_close(circ0.asgate(), circ1.asgate())
write_latex(fname, circ0)
write_latex(fname+'_res', circ1)




fname = 'pauli_deke'
circ0 = qf.Circuit([qf.Rz(Symbol(r'\theta_0'), 0),
                   qf.Ry(Symbol(r'\theta_1'), 0),
                   qf.Rz(Symbol(r'\theta_2'), 0),
                   qf.Ph(Symbol(r'\alpha'), 0)]
                   )
write_latex(fname, circ0)


fname = 'Ph'
circ0 = qf.Circuit(
    qf.Ph(Symbol(r'\alpha'), 0)
    )
write_latex(fname, circ0)


fname = 'PhDeke'
circ0 = qf.Circuit([
    qf.Ph(Symbol(r'-\frac{\theta}{2}'), 0),
    qf.XPow(Symbol(r'\frac{\theta}{\pi}'), 0)
    ])
write_latex(fname, circ0)


print()