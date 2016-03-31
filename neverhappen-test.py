import neverhappen

def test_neverhappen_happens():
  neverhappen.True = False
  assert neverhappen.neverhappen() == "This should never happen"
