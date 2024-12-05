# StockAI

## Postavljanje projekta

Slijedite ove korake kako biste postavili projektno okruženje:

1. Klonirajte repozitorij:
    ```bash
    git clone https://github.com/korisnik/stockai.git
    cd stockai
    ```

2. Instalirajte potrebne pakete koristeći `conda`:
    ```bash
    conda env update --name stockai --file environment.yml --prune
    conda activate stockai
    ```

3. Alternativno, možete koristiti `pip` za instalaciju paketa:
    ```bash
    pip install -r requirements.txt
    ```

4. Provjerite instalaciju PyTorcha:
    ```bash
    python verify_pytorch.py
    ```

5. Pokrenite testni PyTorch skript:
    ```bash
    python test_pytorch.py
    ```
