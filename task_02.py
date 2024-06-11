def coincidence(lst = None, rng = None):
   if lst is None or rng is None:
      return []
   rng_list = list(rng)
   return [x for x in lst if isinstance(x, (int, float)) and (rng_list[0] <= x <= rng_list[-1])]