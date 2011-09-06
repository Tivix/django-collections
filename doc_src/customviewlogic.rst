==================
Custom view logic
==================

Sometimes you need more than just a generic view.  You may find yourself needing to do some extra filtering on your generic objects.

SOLUTION 1
**********
In order to do this, override template_name in the view collection_view.  Within your own template you can customize things any way you want.
You can also pass extra get parameters to the view and filter based on them.

MY QUALMS WITH THIS SOLUTION:
We are going to have to come up with some sort of system for mapping GET parameters to filtering options.
We cannot simply map things one-to-one, as that would reveal far too much of our backend and leave security holes.
We cannot simply encode the parameters, as that would be complicated to implement and code for (and the urls would be ugly).
This means we need a system of conversion from GET parameters to filtering methods.
Such a system is bound to be more complex than writing the corresponding python code in a hook-in function, for both the writer of the system and the coder who eventually uses it.
With National Geographic these filtering options need to include such varied things as filtering by class-type, m2m relations, and custom fields.

SOLUTION 2
In order to do this, you'll need to extend the class-based view DynamicCollectionView.  
DynamicCollectionView has many hook-in functions that allow you change how the view works.
Below are the functions you can override.

.. py:method:: filter_further(self, request, objects)
Filter further takes a request (giving you information to filter on) and expects a queryset in return, so that you can further filter the objects.

Below is an example where we filter based on an extra search parameter
.. code-block:: python
	class CustomCollectionView(DynamicCollectionView):
        
	    def filter_further(self, request, objects):
	        "Override this method if objects needs to be filtered further"
	        return objects.filter(title__contains=request.GET['q'])
*********************************
