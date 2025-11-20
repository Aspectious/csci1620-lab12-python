import pytest
from television import Television

def test_main():
    test_initialization()
    test_channels()
    test_volume()
    test_mute()
    #test_cohesion() -- Commented out due to optionality

def test_initialization():
    # Creates a Television and ensures variables are set to default.
    # Also ensures channel, mute, and volume cannot be changed while the TV is off.
    tv1:Television = Television()
    tv1.volume_up()
    tv1.volume_up()
    tv1.channel_up()
    tv1.channel_up()
    tv1.volume_down()
    tv1.channel_down()
    assert tv1.__str__() == f"Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    tv1.power()
    tv1.volume_up()
    tv1.power()
    tv1.mute()
    assert tv1.__str__() == f"Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME + 1}"

def test_channels():
    tv1:Television = Television()
    tv1.power()
    
    # Checks overflow and underflow for Channels
    for i in range(Television.MAX_CHANNEL - Television.MIN_CHANNEL):
         tv1.channel_up()
    tv1.channel_up()
    assert tv1.__str__() == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    tv1.channel_down()
    assert tv1.__str__() == f"Power = True, Channel = {Television.MAX_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    
def test_volume():
    tv1:Television = Television()
    tv1.power()
    for i in range(Television.MAX_CHANNEL - Television.MIN_CHANNEL):
        tv1.channel_up()

    # Checks inability to surpass volume bounds.
    for i in range (Television.MAX_VOLUME-Television.MIN_VOLUME):
        tv1.volume_up()
    assert tv1.__str__() == f"Power = True, Channel = {Television.MAX_CHANNEL}, Volume = {Television.MAX_VOLUME}"
    tv1.volume_up()
    assert tv1.__str__() == f"Power = True, Channel = {Television.MAX_CHANNEL}, Volume = {Television.MAX_VOLUME}"

    for i in range (Television.MAX_VOLUME - Television.MIN_VOLUME):
        tv1.volume_down()
    assert tv1.__str__() == f"Power = True, Channel = {Television.MAX_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    tv1.volume_down()
    assert tv1.__str__() == f"Power = True, Channel = {Television.MAX_CHANNEL}, Volume = {Television.MIN_VOLUME}"



def test_mute():
    tv1:Television = Television()
    tv1.power()
    for i in range(Television.MAX_CHANNEL-Television.MIN_CHANNEL):
        tv1.channel_up()



    # Checks muting capabilities
    
        # Checks if mute() successfully sets volume to zero, regardless of minimum, and when unmuted, returns to previous value.
    tv1.volume_up()
    tv1.mute()
    assert tv1.__str__() == f"Power = True, Channel = {Television.MAX_CHANNEL}, Volume = 0"
    tv1.mute()
    assert tv1.__str__() == f"Power = True, Channel = {Television.MAX_CHANNEL}, Volume = {Television.MIN_VOLUME + 1}"
    

        # Checks if volume_up() and volume_down() successfully unmutes and executes requested change.
    tv1.mute()
    assert tv1.__str__() == f"Power = True, Channel = {Television.MAX_CHANNEL}, Volume = 0"
    tv1.volume_up()
    assert tv1.__str__() == f"Power = True, Channel = {Television.MAX_CHANNEL}, Volume = {Television.MIN_VOLUME + 2}"
    tv1.mute()
    assert tv1.__str__() == f"Power = True, Channel = {Television.MAX_CHANNEL}, Volume = 0"
    tv1.volume_down()
    assert tv1.__str__() == f"Power = True, Channel = {Television.MAX_CHANNEL}, Volume = {Television.MIN_VOLUME + 1}"
    

#def test_cohesion():
    # Tests if, after a long series of changes, that the Television will retain the correct settings.
    # Note, this test is optional and works best with default settings of 0, 2, 0, 3
#    tv:Television = Television()
#    tv.channel_up()
#    tv.power()
#    tv.channel_up()
#    tv.channel_up()
#    tv.volume_up()
#    tv.volume_up()
#    tv.mute()
#    tv.volume_down()
#    tv.power()
#    tv.channel_up()
#    tv.power()
#    tv.mute()
#    tv.volume_down()
#    tv.volume_up()
#    tv.volume_up()
#    tv.channel_up()
#    tv.power()
#    tv.channel_up()
#    tv.volume_up()
#    tv.mute()
#    tv.power()
#    assert tv.__str__() == f"Power = True, Channel = {Television.MIN_CHANNEL + 3}, Volume = {Television.MIN_VOLUME + 2}"




if __name__ == "__main__":
    test_main()

