# DRF-TODO-API
A simple Django TODO api with authentication


## To install
	*  pip3 install -r requirements.txt

## Packages
	* DRF
	* Django-filters

## API endpoints 
	* `/task` : to view the tasks
	* `/task/<id>`: to get particular task
		* methods: GET, PUT, POST, DELETE
		* filters: 
		* completed: to filter on bases of completed or un completed task
		* search: 
		* task_name: search on bases of task name
	* `/register ` : to register new user
		* methods: POST
		*
