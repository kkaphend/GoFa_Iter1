import compas_rrc as rrc

speed = 50

def send():

    pos = [-10.85, -18.91, 40.09, 15.65, 26.84, 58.71]

    # --- Create Ros Client + ABB Client, and connect
    ros = rrc.RosClient()
    ros.run()
    abb = rrc.AbbClient(ros, '/rob1')
    print('Initialized RosClient and AbbClient.')

    print('Going to start position')
    abb.send_and_wait(rrc.MoveToJoints(pos, [], speed, rrc.Zone.FINE))

    abb.send_and_wait(rrc.PrintText('Finished'))
    print('Finished')

    # --- Close client
    ros.close()
    ros.terminate()


if __name__ == '__main__':
    send()

