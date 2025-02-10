DEFAULT_LVL_EXP = 200

def is_level_up(*, current_exp: int, gained_exp: int) -> bool:
  total_exp = current_exp + gained_exp
  level_up = False

  if total_exp >= DEFAULT_LVL_EXP:
    level_up = True

  return level_up


print(is_level_up(current_exp=150, gained_exp=60))
print(is_level_up(current_exp=10, gained_exp=60))