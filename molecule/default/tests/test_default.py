import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_dockerd_running_and_enabled(host):
    service = host.service('docker')
    assert service.is_enabled
    assert service.is_running

# TODO: why not listen?
# def test_dockerd_is_listen(host):
#     socket = host.socket('unix:///run/docker.sock')
#     assert socket.is_listening

# def test_containerd_is_listen(host):
#     socket = host.socket('unix:///run/containerd/containerd.sock')
#     assert socket.is_listening
