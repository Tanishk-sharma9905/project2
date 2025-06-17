# Pokémon Data Collection Project

This project extracts detailed Pokémon data from the [PokéAPI](https://pokeapi.co/), processes it using Python, and stores it in a MySQL database. The final dataset includes attributes like ID, name, types, abilities, moves, and base stats for each Pokémon, and is published on [Kaggle](https://www.kaggle.com/datasets/tanishksharma9905/pokemon-data-csv).

---

## 📌 Features

* ✅ Fetches all Pokémon using the PokéAPI.
* ✅ Extracts and structures key information:

  * `id`, `name`, `base_experience`, `height`, `weight`
  * `types`, `abilities`, top 5 `moves`
  * Base `stats` (e.g., attack, defense)
* ✅ Stores data in a **MySQL** database via **SQLAlchemy**.
* ✅ Logging included for traceability.
* ✅ Final dataset exported and published on Kaggle.

---

## 📂 Dataset Structure

| Column            | Description                               |
| ----------------- | ----------------------------------------- |
| `id`              | Unique identifier for the Pokémon         |
| `name`            | Name of the Pokémon                       |
| `base_experience` | Base experience points                    |
| `height`          | Height (in decimetres)                    |
| `weight`          | Weight (in hectograms)                    |
| `types`           | Pokémon types (e.g., Grass, Poison)       |
| `abilities`       | List of Pokémon abilities                 |
| `moves`           | Top 5 moves listed for the Pokémon        |
| `stats`           | Base stats like hp, attack, defense, etc. |

---

## 🚀 Technologies Used

* `Python 3`
* `Pandas`
* `SQLAlchemy`
* `MySQL`
* `Requests`
* `Logging`

---

## 🛠️ Setup Instructions

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/pokemon-data-pipeline.git
   cd pokemon-data-pipeline
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure MySQL connection string:

   ```python
   con_string = "mysql+pymysql://<user>:<password>@localhost/<database>"
   ```

4. Run the script:

   ```bash
   python pokemon_etl.py
   ```

---

## 📁 Output

* A structured CSV dataset: [Kaggle Link](https://www.kaggle.com/datasets/tanishksharma9905/pokemon-data-csv)
* Logged actions stored in: `logs/project2.log`

---

## 📄 License

This project is open-source under the MIT License.
API data provided by [PokéAPI](https://pokeapi.co/).

---

## 🙌 Acknowledgements

* [PokéAPI](https://pokeapi.co/) – for providing the Pokémon data
* Kaggle – for hosting the dataset
