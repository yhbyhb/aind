# %% Bayes Network
p_c = 0.01
p_p_c = 0.9
p_m_not_c = 0.8
p_not_c = 0.99
p_m_c = 0.1
p_p_not_c = 0.2

pp_c_p_p = p_c * p_p_c * p_p_c
pp_not_c_p_p = p_not_c * p_p_not_c * p_p_not_c

print(pp_c_p_p, pp_not_c_p_p)
print(pp_c_p_p / (pp_c_p_p + pp_not_c_p_p))
# %%
pp_c_p_m = p_c * p_p_c * p_m_c
pp_not_c_p_m = p_not_c * p_p_not_c * p_m_not_c

print(pp_c_p_m, pp_not_c_p_m)
print(pp_c_p_m / (pp_c_p_m + pp_not_c_p_m))
# %% 8. Quiz : Conditional Independence 2
pp_c_p = p_c * p_p_c
pp_not_c_p = p_not_c * p_p_not_c

p_c_p = pp_c_p / (pp_c_p + pp_not_c_p_p)
p_not_c_p = pp_not_c_p / (pp_c_p + pp_not_c_p_p)
print(p_c_p, p_not_c_p)

p_p_p = p_p_c * p_c_p + p_p_not_c * p_not_c_p
print(f'{p_p_p:0.3F}')
# %% 11. Quiz: Explaining Away p_r_h_s ?
p_s = 0.7
p_not_s = 1 - p_s
p_r = 0.01
p_not_r = 1 - p_r
p_h_r_s = 1
p_h_not_s_r = 0.9
p_h_s_not_r = 0.7
p_h_not_r_s = p_h_s_not_r
p_h_not_s_not_r = 0.1

#p_r_h_s = p_h_r_s * p_r_s / p_h_s
p_r_h_s = p_h_r_s * p_r / (p_h_r_s * p_r + p_h_not_r_s * p_not_r)
print(p_r_h_s)
# %% 12 Quiz: Explaining Away 2 p_r_h ?
p_h = p_h_r_s * p_r * p_s + \
      p_h_not_r_s * p_not_r * p_s + \
      p_h_s_not_r * p_r * p_not_s + \
      p_h_not_s_not_r * p_not_r * p_not_s

#p_r_h = p_h_r * p_r / p_h
p_r_h = (p_h_r_s * p_s + p_h_not_s_r * p_not_s) * p_r / p_h
print(f'{p_r_h:0.4F}')
# %% 13 Quiz: Explaining Away 3 p_r_h_not_s
# p_r_h_not_s = p_h_r_not_s * p_r_not_s / p_h_not_s
p_r_h_not_s = 0.9 * 0.01 / (p_h_not_s_r * p_r + p_h_not_s_not_r * p_not_r)
print(f'{p_r_h_not_s:0.4F}')
# %%
