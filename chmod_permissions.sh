#!/bin/bash

# Script to change permissions for a selected folder

# Prompt the user to specify the folder
echo "Enter the folder name (default: ny_taxi_postgres_data):"
read input_folder

# Use the provided folder name or default to ny_taxi_postgres_data
db_folder=${input_folder:-ny_taxi_postgres_data}
user_name=$(whoami)

echo "Selected folder: $db_folder"

echo "Available options:"
echo "1. Assign permissions to the current user ($user_name)"
echo "2. Restore default permissions for PostgreSQL (999:999)"
echo "3. Exit"

read -p "Choose an option (1, 2, or 3): " option

case $option in
    1)
        echo "Changing permissions for user: $user_name"
        sudo chown -R $user_name:$user_name $db_folder
        sudo chmod -R 700 $db_folder
        echo "Permissions updated for user $user_name."
        ;;
    2)
        echo "Restoring default permissions for PostgreSQL (999:999)"
        sudo chown -R 999:999 $db_folder
        sudo chmod -R 700 $db_folder
        echo "Permissions restored for PostgreSQL."
        ;;
    3)
        echo "Exiting script."
        exit 0
        ;;
    *)
        echo "Invalid option. Please choose 1, 2, or 3."
        ;;
esac
