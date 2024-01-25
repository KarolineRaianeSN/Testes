# Mp = [(N1 * P1) + (N2 * P2) + ... + (Nx * Px)] / (P1 + P2 + ... + Px)

def main():
    A = float(input())
    B = float(input())
    C = float(input())
    media = ((A * 2) + (B * 3) + (C * 5)) / 10

    print(f'MEDIA = {media:.1f}')


main()