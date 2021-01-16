import eel
import dbus, dbus.mainloop.glib, sys
from gi.repository import GLib

def main():
    # Setup
    eel.init("web")

    # Functions
    @eel.expose
    def helloWorld():
        print("Hello world!")

    @eel.expose
    def btPlay():
        print("Play")

    @eel.expose
    def btPause():
        print("Pause")

    # Start
    eel.start("index.html", mode="chrome", lock=False, size=(800, 480), port=2804)

    # Run Once


    # Main Loop
    while True:
        eel.sleep(1)



def onPropertyChanged(interface, changed, invalidated):
    if interface != 'org.bluez.MediaPlayer1':
        return
    for prop, value in changed.items():
        if prop == 'Status':
            print('Playback Status: {}'.format(value))
        elif prop == 'Track':
            print('Music Info:')
            for key in ('Title', 'Artist', 'Album'):
                print('   {}: {}'.format(key, value.get(key, '')))

def onPlaybackControl(command):
    if command.startswith('play'):
        player_iface.Play()
    elif command.startswith('pause'):
        player_iface.Pause()
    elif command.startswith('next'):
        player_iface.Next()
    elif command.startswith('prev'):
        player_iface.Previous()
    elif command.startswith('vol'):
        vol = int(str.split()[1])
        if vol not in range(0, 128):
            print('Possible Values: 0-127')
            return
        transport_prop_iface.Set(
                'org.bluez.MediaTransport1',
                'Volume',
                dbus.UInt16(vol))


if __name__ == '__main__':
    # Init Bluetooth Control
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    obj = bus.get_object('org.bluez', "/")
    mgr = dbus.Interface(obj, 'org.freedesktop.DBus.ObjectManager')
    player_iface = None
    transport_prop_iface = None
    for path, ifaces in mgr.GetManagedObjects().items():
        if 'org.bluez.MediaPlayer1' in ifaces:
            player_iface = dbus.Interface(
                    bus.get_object('org.bluez', path),
                    'org.bluez.MediaPlayer1')
        elif 'org.bluez.MediaTransport1' in ifaces:
            transport_prop_iface = dbus.Interface(
                    bus.get_object('org.bluez', path),
                    'org.freedesktop.DBus.Properties')
    if not player_iface:
        sys.exit('Error: Media Player not found.')
    if not transport_prop_iface:
        sys.exit('Error: DBus.Properties iface not found.')

    bus.add_signal_receiver(
            onPropertyChanged,
            bus_name='org.bluez',
            signal_name='PropertiesChanged',
            dbus_interface='org.freedesktop.DBus.Properties')
    GLib.MainLoop().run()

    # Main
    main()