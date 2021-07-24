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

q0, q1, q2 = 0, 1, 2


def write_latex(fname, circ):
    # scale = 0.75
    latex = qf.circuit_to_latex(circ, document=False, package='quantikz',
                                qubit_labels=False, scale=0.8)
    with open(fname + '.tex', "w") as fout:
        fout.write(latex)

    print('.', end='')


fname = 'margolus_to_cnot'
gate = qf.Margolus(q0, q1, q2)
circ = qf.Circuit(qf.translate_margolus_to_cnot(gate))
write_latex(fname, circ)

fname = 'margolus_to_ccnot'
gate = qf.Margolus(q0, q1, q2)
circ = qf.Circuit([qf.X(q1), qf.CCZ(0, 1, 2), qf.X(q1), qf.CCNot(q0, q1,q2)]) 
write_latex(fname, circ)



fname = 'cnot'
circ = qf.Circuit([qf.CNot(0, 1)])
write_latex(fname, circ)

fname = 'cnot_10'
circ = qf.Circuit([qf.CNot(1, 0)])
write_latex(fname, circ)

fname = 'cnot_switch'
circ = qf.Circuit([qf.H(0), qf.H(1), qf.CNot(0, 1), qf.H(0), qf.H(1)])
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

fname = 'cy'
circ = qf.Circuit([qf.CY(0, 1)])
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

fname = 'cnot_to_cy'
circ = qf.Circuit(qf.translate_cy_to_cnot(qf.CY(0, 1)))
write_latex(fname, circ)

fname = 'ccnot'
circ = qf.Circuit([qf.CCNot(0, 1, 2)])
write_latex(fname, circ)

fname = 'ccnot_to_cnot'
circ = qf.Circuit(qf.translate_ccnot_to_cnot(qf.CCNot(0, 1, 2)))
write_latex(fname, circ)

fname = 'cswap_to_ccnot'
circ = qf.Circuit(qf.translate_cswap_to_ccnot(qf.CSwap(0, 1, 2)))
write_latex(fname, circ)

fname = 'cswap_to_adjacent_cnot'
circ = qf.Circuit(qf.translate_cswap_to_cnot(qf.CSwap(0, 1, 2)))
write_latex(fname, circ)

fname = 'cswap_to_inside_cnot'
circ = qf.Circuit(qf.translate_cswap_inside_to_cnot(qf.CSwap(0, 1, 2)))
write_latex(fname, circ)

fname = 'syc'
circ = qf.Circuit([qf.Sycamore(0, 1)])
write_latex(fname, circ)


fname = 'syc_to_can'
circ = qf.Circuit(qf.translate_syc_to_can(qf.Sycamore(0, 1)))
write_latex(fname, circ)



fname = 'ccnot_to_adjacent_cnot'
circ = qf.Circuit(qf.H(2)) + qf.Circuit(qf.translate_ccz_to_adjacent_cnot(qf.CCNot(0, 1, 2))) + qf.Circuit(qf.H(2))
write_latex(fname, circ)

fname = 'ccz'
circ = qf.Circuit(qf.CCZ(0, 1, 2))
write_latex(fname, circ)


fname = 'ccnot_to_cv'
circ = qf.Circuit(qf.translate_ccnot_to_cv(qf.CCNot(0, 1, 2)))
write_latex(fname, circ)


fname = 'ccnot_to_cnot_AMMR'
circ = qf.Circuit(qf.translate_ccnot_to_cnot_AMMR(qf.CCNot(0, 1, 2)))
write_latex(fname, circ)

fname = 'cnot_to_ccz'
circ = qf.Circuit([qf.H(2), qf.CCNot(0, 1, 2), qf.H(2)])
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
circ = qf.Circuit([qf.XX(t, 0, 1, )])
write_latex(fname, circ)

fname = 'yy'
circ = qf.Circuit([qf.YY(t, 0, 1, )])
write_latex(fname, circ)

fname = 'zz'
circ = qf.Circuit([qf.ZZ(t, 0, 1, )])
write_latex(fname, circ)

fname = 'RX'
circ = qf.Circuit([qf.Rx(theta, 0)])
write_latex(fname, circ)

fname = 'RX0_RX_1'
circ = qf.Circuit([qf.Rx(Symbol(r'\theta_0'), 0), qf.Rx(Symbol(r'\theta_1'), 0)])
write_latex(fname, circ)

fname = 'RX01'
circ = qf.Circuit(qf.Rx(Symbol(r'\theta_{0}+\theta_{1}'), 0))
write_latex(fname, circ)


fname = 'RY0_RY_1'
circ = qf.Circuit([qf.Ry(Symbol(r'\theta_0'), 0), qf.Ry(Symbol(r'\theta_1'), 0)])
write_latex(fname, circ)

fname = 'RY01'
circ = qf.Circuit(qf.Ry(Symbol(r'\theta_{0}+\theta_{1}'), 0))
write_latex(fname, circ)


fname = 'RZ0_RZ_1'
circ = qf.Circuit([qf.Rz(Symbol(r'\theta_{0}'), 0), qf.Rz(Symbol(r'\theta_{1}'), 0)])
write_latex(fname, circ)

fname = 'RZ01'
circ = qf.Circuit(qf.Rz(Symbol(r'\theta_{0}+\theta_{1}'), 0))
write_latex(fname, circ)


fname = 'RY'
circ = qf.Circuit([qf.Ry(theta, 0)])
write_latex(fname, circ)

fname = 'RZ'
circ = qf.Circuit([qf.Rz(theta, 0)])
write_latex(fname, circ)

fname = 'XPow'
circ = qf.Circuit([qf.XPow(t, 0)])
write_latex(fname, circ)

fname = 'YPow'
circ = qf.Circuit([qf.YPow(t, 0)])
write_latex(fname, circ)

fname = 'ZPow'
circ = qf.Circuit([qf.ZPow(t, 0)])
write_latex(fname, circ)

# fname = 'phadamard'
# circ = qf.Circuit([qf.Unitary(name='h', qubits=[0], tensor=qf.I(0).tensor)])
# write_latex(fname, circ)

# fname = 'inv_phadamard'
# circ = qf.Circuit([qf.Unitary(name=Symbol(r'h$^\dagger$'),
#                               qubits=[0], tensor=qf.I(0).tensor)])
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

deutsch = qf.Deutsch(theta, 0, 1, 2)
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


fname = 'cphase'
circ = qf.Circuit([qf.CPhase(theta)])
write_latex(fname, circ)




fname = 'cphase_to_zz'
circ = qf.Circuit(qf.translate_cphase_to_zz(qf.CPhase(theta)))
write_latex(fname, circ)


fname = 'cphase00_to_cphase'
circ = qf.Circuit(qf.translate_cphase00_to_cphase(qf.CPhase00(theta)))
write_latex(fname, circ)

fname = 'cphase01_to_cphase'
circ = qf.Circuit(qf.translate_cphase01_to_cphase(qf.CPhase01(theta)))
write_latex(fname, circ)

fname = 'cphase10_to_cphase'
circ = qf.Circuit(qf.translate_cphase10_to_cphase(qf.CPhase10(theta)))
write_latex(fname, circ)




fname = 'can_decrement'
circ = qf.Circuit([qf.Y(q0), qf.Y(q1), qf.Can(tx, ty, tz, q0, q1), qf.Z(q0), qf.Z(q1)])
write_latex(fname, circ)

fname = 'can_decrement_res'
circ = qf.Circuit([qf.Can(tx-1, ty, tz, q0, q1)])
write_latex(fname, circ)


fname = 'can_flip'
circ = qf.Circuit([qf.Z(q0), qf.Can(tx, ty, tz, q0, q1), qf.Z(q0)])
write_latex(fname, circ)

fname = 'can_flip_res'
circ = qf.Circuit([qf.Can(-tx, -ty, tz, q0, q1)])
write_latex(fname, circ)

fname = 'can_swap'
circ = qf.Circuit([qf.S(q0), qf.S(q1), qf.Can(tx, ty, tz, q0, q1), qf.S_H(q0), qf.S_H(q1)])
write_latex(fname, circ)

fname = 'can_swap_res'
circ = qf.Circuit([qf.Can(ty, tx, tz, q0, q1)])
write_latex(fname, circ)


fname = 'can_bot'
circ = qf.Circuit([qf.Y(q1), qf.Can(tx, ty, 0, q0, q1), qf.Z(q0), qf.Y(q0), qf.Z(q1)])
write_latex(fname, circ)

fname = 'can_bot_res'
circ = qf.Circuit([qf.Can(1-tx, ty, 0, q0, q1)])
write_latex(fname, circ)

fname = 'can_sum'
circ = qf.Circuit([qf.Can(sx, sy, sz, q0, q1), qf.Can(tx, ty, tz, q0, q1)])
write_latex(fname, circ)

fname = 'can_sum_res'
circ = qf.Circuit([qf.Can(tx+sx, ty+sy, tz+sz, q0, q1)])
write_latex(fname, circ)

fname = 'ccix'
gate = qf.CCiX(0, 1, 2)
circ = qf.Circuit([gate])
write_latex(fname, circ)

fname = 'ccix_to_cnot'
circ = qf.Circuit(qf.translate_ccix_to_cnot(gate))
write_latex(fname, circ)

fname = 'ccix_to_cnot_adjacent'
circ = qf.Circuit(qf.translate_ccix_to_cnot_adjacent(gate))
write_latex(fname, circ)

fname = 'ciswap'
gate = qf.CISwap(0, 1, 2)
circ = qf.Circuit([gate])
# write_latex(fname, circ)

fname = 'ciswap_to_ccix'
circ = qf.Circuit(qf.translate_ciswap_to_ccix(gate))
write_latex(fname, circ)


fname = "can"
gate = qf.Can(tx, ty, tz, q0, q1)
write_latex(fname, qf.Circuit(gate))

fname = "can_to_cnot"
circ = qf.Circuit(qf.translate_can_to_cnot(gate))
write_latex(fname, circ)


fname = "can_so"
gate = qf.Can(tx, ty, 0, q0, q1)
write_latex(fname, qf.Circuit(gate))

fname = "can_to_2cnot"
circ = qf.Circuit(qf.translate_can_to_cnot(gate))
write_latex(fname, circ)

fname ="can_io"
gate = qf.Can(1/2, ty, tz, q0, q1)
write_latex(fname, qf.Circuit(gate))

fname = "can_to_2cnot_swap"
circ = qf.Circuit([qf.H(0), qf.H(1), qf.V(0).H, qf.V(1).H,qf.CNot(0,1), qf.X(0)**(tz-1/2), qf.Z(1) ** (ty-1/2), qf.CNot(0, 1), qf.Swap(0,1), qf.V(0), qf.V(1), qf.H(0), qf.H(1)])
write_latex(fname, circ)
# print(qf.canonical_decomposition(circ.asgate()))
# assert qf.gates_close(circ.asgate(), qf.Can(0.5, ty, tz, 0, 1))


fname ="can_cnot"
gate = qf.Can(1/2, 0, 0, q0, q1)
write_latex(fname, qf.Circuit(gate))

fname ="can_to_1cnot"
circ = qf.Circuit([  qf.H(q0), qf.H(q1) ,qf.S(q0) ,qf.S(q1) ,qf.H(q1), qf.CNot(0, 1), qf.H(q0)])
write_latex(fname, circ)

fname = 'pauli_deke'
circ0 = qf.Circuit([qf.Rz(Symbol(r'\theta_0'), 0),
                   qf.Ry(Symbol(r'\theta_1'), 0),
                   qf.Rz(Symbol(r'\theta_2'), 0),
                   qf.Ph(alpha, 0)]
                   )
write_latex(fname, circ0)


fname = 'Ph'
circ0 = qf.Circuit(
    qf.Ph(alpha, 0)
    )
write_latex(fname, circ0)


fname = 'PhDeke'
circ0 = qf.Circuit([
    qf.Ph(Symbol(r'-\frac{\theta}{2}'), 0),
    qf.XPow(Symbol(r'\frac{\theta}{\pi}'), 0)
    ])
write_latex(fname, circ0)


fname = 'a_to_cnot'
circ = qf.Circuit(qf.translate_a_to_cnot(qf.A(theta, phi, 0, 1)))
write_latex(fname, circ)

fname = 'a_to_can'
circ = qf.Circuit(qf.translate_a_to_can(qf.A(theta, phi, 0, 1)))
write_latex(fname, circ)

fname = 'barenco_to_xx'
circ = qf.Circuit(qf.translate_barenco_to_xx(qf.Barenco(phi, alpha, theta, 0, 1)))
write_latex(fname, circ)




fname = "ch"
gate = qf.CH(q0, q1)
write_latex(fname, qf.Circuit(gate))

fname = "ch_to_cnot"
circ = qf.Circuit(qf.translate_ch_to_cpt(gate))
write_latex(fname, circ)


fname = "givens_to_xy"
gate = qf.Givens(theta, q0, q1)
circ = qf.Circuit(qf.translate_givens_to_xy(gate))
write_latex(fname, circ)

fname = "xy"
gate = qf.XY(t, q0, q1)
circ = qf.Circuit(gate)
write_latex(fname, circ)








print()