# Project data

Keep original inputs in `raw/` and derived datasets in `processed/`. Do not overwrite original inputs. Data outside the project may stay there; document their location and configure access separately.

For each source, record:

- Source, version or retrieval date, and documentation.
- How authorised researchers can obtain it.
- Access and sharing restrictions, including whether it may be supplied to an AI service.
- The scripts or notebooks that produce processed data and the order to run them.

Data files are not ignored by default. Review files before staging: do not commit sensitive or large datasets. Git exclusion rules do not control agent access.
