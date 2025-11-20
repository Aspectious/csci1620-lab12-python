

class Television:
    """
    Defines all the required components of a television.

    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        """
            Creates and Initializes TV with default instance variables.
            By default, the TV is off, unmuted, 
            with Volume at MIN_VOLUME tuned to MIN_CHANNEL.

            Args:
                None
            Returns:
                this:Television
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
            Toggles the power of the TV.
            Will run regardless of power or state.

            Args:
                None
            Returns:
                None
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
            Toggles mute on the TV.
            Does not run if TV is off.

            Args:
                None
            Returns:
                None
        """
        if (self.__status == False):
            return
        else:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
            Increases the channel number by one.
            Overflows if run at MAX_CHANNEL.
            Does not run if TV is off.

            Args:
                None
            Returns:
                None
        """
        if (self.__status == False):
            return
        if (self.__channel == Television.MAX_CHANNEL):
            self.__channel = Television.MIN_CHANNEL
        else:
            self.__channel += 1

    def channel_down(self) -> None:
        """
            Lowers the TV's channel by one.
            Underflows if at MIN_CHANNEL.
            Does not run if TV is off.

            Args:
                None
            Returns:
                None
        """
        if (self.__status == False):
            return
        if (self.__channel == Television.MIN_CHANNEL):
            self.__channel = Television.MAX_CHANNEL
        else:
            self.__channel -= 1

    def volume_up(self) -> None:
        """
            Raises the TV's volume by one, unless it is at MAX_VOLUME.
            Unmutes TV if run while muted.
            Not run if TV is off.

            Args:
                None
            Returns:
                None
        """
        if (self.__status == False):
            return
        if (self.__muted == True):
            self.__muted = False
        if (self.__volume == Television.MAX_VOLUME):
            self.__volume = self.__volume
        else:
            self.__volume += 1


    def volume_down(self) -> None:
        """
            Lowers the TV's volume by one, unless it is at MIN_VOLUME.
            Unmutes TV if run while muted.
            Not run if TV is off.

            Args:
                None
            Returns:
                None

        """
        if (self.__status == False):
            return
        if (self.__muted == True):
            self.__muted = False
        if (self.__volume == Television.MIN_VOLUME):
            self.__volume = self.__volume
        else:
            self.__volume -= 1

    def __str__(self)-> str:
        """
            Returns this object as a string.
            
            Formatted as:
                "Power = [bool], Channel = [int], Volume = [int]"

            Args:
                None
            Returns:
               Television Information as String. 

        """
        displayVolume:int = self.__volume
        if (self.__muted):
            displayVolume = 0
        output = f"Power = {self.__status}, Channel = {self.__channel}, Volume = {displayVolume}"
        return output
