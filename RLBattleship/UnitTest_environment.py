import environment as env

ut_env = env.Environment(size=(5,5))
ut_env.set_starting_state()
assert ut_env.game_state == "0000000000000000000000000"
ut_env.ship_state = "000000sss0000000000000000"
# print("ship state 1")
# ut_env.pretty_print_state(ut_env.ship_state)
# print("game state 1")
# ut_env.pretty_print_state(ut_env.game_state)
new_state, reward, game_end = ut_env.mark(3,2)
# print("new state")
# ut_env.pretty_print_state(new_state)
try:
    assert new_state == "0000000h00000000000000000"
    print("Test #1 Passed")
except Exception as e:
    print("Expected:\t0000000h00000000000000000\nGot:\t\t"+new_state)

try:
    assert ut_env.ship_state == "000000shs0000000000000000"
    print("Test #2 Passed")
except Exception as e:
    print("Expected:\t000000shs0000000000000000\nGot:\t\t"+ut_env.ship_state)

try:
    assert game_end == False
    print("Test #3 Passed")
except Exception as e:
    print("Expected:\tFalse\nGot:\t\t"+str(game_end))

try:
    assert reward == 10
    print("Test #4 Passed")
except Exception as e:
    print("Expected:\t10\nGot:\t\t"+str(reward))

new_state, reward, game_end = ut_env.mark(4,2)
# print("new state")
# ut_env.pretty_print_state(new_state)
try:
    assert new_state == "0000000hh0000000000000000"
    print("Test #5 Passed")
except Exception as e:
    print("Expected:\t0000000hh0000000000000000\nGot:\t\t"+new_state)

try:
    assert ut_env.ship_state == "000000shh0000000000000000"
    print("Test #6 Passed")
except Exception as e:
    print("Expected:\t000000shh0000000000000000\nGot:\t\t"+ut_env.ship_state)

try:
    assert game_end == False
    print("Test #7 Passed")
except Exception as e:
    print("Expected:\tFalse\nGot:\t\t"+str(game_end))

try:
    assert reward == 10
    print("Test #8 Passed")
except Exception as e:
    print("Expected:\t10\nGot:\t\t"+str(reward))

new_state, reward, game_end = ut_env.mark(4,3)
# print("new state")
# ut_env.pretty_print_state(new_state)
try:
    assert new_state == "0000000hh0000m00000000000"
    print("Test #9 Passed")
except Exception as e:
    print("Expected:\0000000hh0000m00000000000\nGot:\t\t"+new_state)

try:
    assert ut_env.ship_state == "000000shh0000000000000000"
    print("Test #10 Passed")
except Exception as e:
    print("Expected:\t000000shh0000000000000000\nGot:\t\t"+ut_env.ship_state)

try:
    assert game_end == False
    print("Test #11 Passed")
except Exception as e:
    print("Expected:\tFalse\nGot:\t\t"+str(game_end))

try:
    assert reward == -1
    print("Test #12 Passed")
except Exception as e:
    print("Expected:\t-1\nGot:\t\t"+str(reward))

new_state, reward, game_end = ut_env.mark(2,2)
# print("new state")
# ut_env.pretty_print_state(new_state)
try:
    assert new_state == "000000hhh0000m00000000000"
    print("Test #13 Passed")
except Exception as e:
    print("Expected:\000000hhh0000m00000000000\nGot:\t\t"+new_state)

try:
    assert ut_env.ship_state == "000000hhh0000000000000000"
    print("Test #14 Passed")
except Exception as e:
    print("Expected:\t000000hhh0000000000000000\nGot:\t\t"+ut_env.ship_state)

try:
    assert game_end == True
    print("Test #15 Passed")
except Exception as e:
    print("Expected:\tTrue\nGot:\t\t"+str(game_end))

try:
    assert reward == 100
    print("Test #16 Passed")
except Exception as e:
    print("Expected:\t100\nGot:\t\t"+str(reward))

new_state, reward, game_end = ut_env.mark(1,1)
# print("new state")
# ut_env.pretty_print_state(new_state)
try:
    assert new_state == "000000hhh0000m00000000000"
    print("Test #17 Passed")
except Exception as e:
    print("Expected:\000000hhh0000m00000000000\nGot:\t\t"+new_state)

try:
    assert ut_env.ship_state == "000000hhh0000000000000000"
    print("Test #18 Passed")
except Exception as e:
    print("Expected:\t000000hhh0000000000000000\nGot:\t\t"+ut_env.ship_state)

try:
    assert game_end == True
    print("Test #19 Passed")
except Exception as e:
    print("Expected:\tTrue\nGot:\t\t"+str(game_end))

try:
    assert reward == 0
    print("Test #20 Passed")
except Exception as e:
    print("Expected:\t100\nGot:\t\t"+str(reward))