from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.io import output_file
from bokeh.palettes import Category10

def plot_route(route, title='TSP Route', show_progress=False, progress=None):
    x_coords = [city.x for city in route.cities]
    y_coords = [city.y for city in route.cities]
    
    # Add the first city at the end to complete the loop
    x_coords.append(x_coords[0])
    y_coords.append(y_coords[0])
    
    # Create a data source for the cities
    city_source = ColumnDataSource(data=dict(
        x=x_coords[:-1],
        y=y_coords[:-1],
        index=list(range(len(x_coords)-1))
    ))
    
    # Create a data source for the route
    route_source = ColumnDataSource(data=dict(
        x=x_coords,
        y=y_coords
    ))
    
    # Create the figure
    p = figure(title=title, x_axis_label='X', y_axis_label='Y',
              tools='pan,wheel_zoom,box_zoom,reset,save')
    
    # Add hover tool for cities
    hover = HoverTool(tooltips=[
        ('City', '@index'),
        ('X', '@x'),
        ('Y', '@y')
    ])
    p.add_tools(hover)
    
    # Plot the cities
    p.circle('x', 'y', size=10, color='red', source=city_source)
    
    # Plot the route
    p.line('x', 'y', line_width=2, source=route_source)
    
    # If progress data is provided, create a second plot
    if show_progress and progress is not None:
        from bokeh.layouts import gridplot
        
        # Create progress plot
        progress_source = ColumnDataSource(data=dict(
            iteration=list(range(len(progress))),
            distance=progress
        ))
        
        p2 = figure(title='Optimization Progress', x_axis_label='Iteration',
                   y_axis_label='Distance', tools='pan,wheel_zoom,box_zoom,reset,save')
        p2.line('iteration', 'distance', line_width=2, source=progress_source)
        
        # Combine plots
        return gridplot([[p], [p2]])
    
    return p
