# Aluno: Victor Alves Freire De Queiroz
# Matrícula: 202307122

import numpy as np
import control as ct
import matplotlib.pyplot as plt

s = ct.tf('s')
G = 20 / (s * (s + 2) * (s + 4))
H = 1

# sem compensação
mf0 = ct.feedback(G, H)
polos0 = ct.poles(mf0)
pc = polos0[np.argmax(np.abs(polos0.imag))]
sigma = -pc.real
wd = abs(pc.imag)
print("Polos sem compensação:", np.round(polos0, 4))
print(f"sigma = {sigma:.4f}  Ts teórico = {4/sigma:.4f} s")

mss = 0.25
zeta = -np.log(mss) / np.sqrt(np.pi**2 + np.log(mss)**2)
sigma_novo = 2 * sigma
wn = sigma_novo / zeta
wd_novo = wn * np.sqrt(1 - zeta**2)
s1 = complex(-sigma_novo, wd_novo)
print(f"\nzeta = {zeta:.4f}  wn = {wn:.4f} rad/s")
print(f"Polo desejado: s1 = {s1.real:.4f} ± j{s1.imag:.4f}")

T = 1 / 2

ang = np.degrees(np.angle(s1) + np.angle(s1 + 4))
ang_polo = 180 - ang
p = -s1.real + s1.imag / np.tan(np.radians(ang_polo))
alfa = (1 / T) / p
print(f"\nContribuição do polo de C(s) = {ang_polo:.4f} graus")
print(f"Polo de C(s) em s = {-p:.4f}")

# condição de módulo
K = abs(s1) * abs(s1 + p) * abs(s1 + 4) * alfa / 20

print(f"\nK    = {K:.4f}")
print(f"alfa = {alfa:.4f}")
print(f"T    = {T:.4f}")

C = K * (1 + s*T) / (1 + s*alfa*T)
print(f"\nC(s) = {K/alfa:.4f} (s + {1/T:.0f}) / (s + {p:.4f})")

mf = ct.feedback(C * G, H)
print("Polos com compensação:", np.round(ct.poles(mf), 4))

t = np.linspace(0, 20, 20000)
t0, y0 = ct.step_response(mf0, t)
t1, y1 = ct.step_response(mf, t)

info0 = ct.step_info(mf0, T=t, SettlingTimeThreshold=0.02)
info1 = ct.step_info(mf, T=t, SettlingTimeThreshold=0.02)

print("\nSem compensação (C=1):")
print(f"  Mp = {info0['Overshoot']:.2f} %")
print(f"  Ts = {info0['SettlingTime']:.4f} s")
print(f"  Tp = {info0['PeakTime']:.4f} s")

print("\nCom compensador avanço:")
print(f"  Mp = {info1['Overshoot']:.2f} %")
print(f"  Ts = {info1['SettlingTime']:.4f} s")
print(f"  Tp = {info1['PeakTime']:.4f} s")

print(f"\nRazão Ts: {info0['SettlingTime']/info1['SettlingTime']:.2f}x menor")

plt.figure(figsize=(9, 5))
plt.plot(t0, y0, label='Sem compensação (C=1)')
plt.plot(t1, y1, label='Com compensador avanço')
plt.xlabel('Tempo (s)')
plt.ylabel('y(t)')
plt.title('Resposta ao degrau unitário')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('resposta_degrau_avanco.png', dpi=120)
plt.show()
