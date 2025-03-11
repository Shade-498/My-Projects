import speedtest


def measuare_speedtest():
    st = speedtest.Speedtest() # Speedtest object
    st.get_best_server()  # Get the best server for testing

    download_speed = st.download() / 10**6  # Convert to Mbps
    print((f"Download Speed: {download_speed:.2f} Mbps"))

    upload_speed = st.upload() / 10**6  # Convert to Mbps
    print((f"Upload Speed: {upload_speed:.2f} Mbps"))

    ping = st.results.ping
    print((f"Ping: {ping:.2f} ms"))


if __name__ == "__main__":
    measuare_speedtest()