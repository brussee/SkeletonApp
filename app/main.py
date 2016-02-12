import libtorrent as lt
import time

ses = lt.session()
ses.listen_on(6881, 6891)

e = lt.bdecode(open("/storage/emulated/0/Torrents/ubuntu-15.10-desktop-amd64.iso.torrent", 'rb').read())
info = lt.torrent_info(e)

params = { 'save_path': '/storage/emulated/0/Torrents/', \
           'storage_mode': lt.storage_mode_t.storage_mode_sparse, \
           'ti': info }
h = ses.add_torrent(params)

s = h.status()
while (not s.is_seeding):
        s = h.status()

        state_str = ['queued', 'checking', 'downloading metadata', \
                'downloading', 'finished', 'seeding', 'allocating']
        print '%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %d' % \
                (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
                s.num_peers, s.state)

        time.sleep(1)