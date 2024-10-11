{{ config(materialized='table') }}

SELECT
    1 AS id,
    'Sample Name' AS name,
    'Sample Value' AS value