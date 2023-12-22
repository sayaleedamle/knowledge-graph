import networkx as nx
import matplotlib.pyplot as plt

import knowledge_graph.backend.create_ontology as ontology

def create_network(ontology_relations: list):
    
    G = nx.Graph()
    for i in ontology_relations:
        src = i.get('Source')
        target = i.get('Target')
        attribute = i.get('Relation Name')
        G.add_edge(src, target, relation= attribute)
    return G

if __name__ == '__main__':
    
    lst = [{'Source': 'Car', 'Target': 'Motor vehicle', 'Relation Name': 'isA'}, {'Source': 'Car', 'Target': 'Wheels', 'Relation Name': 'has'}, {'Source': 'Car', 'Target': 'Roads', 'Relation Name': 'runsOn'}, {'Source': 'Car', 'Target': 'People', 'Relation Name': 'transports'}, {'Source': 'Car', 'Target': 'Cargo', 'Relation Name': 'doesNotMainlyTransport'}, {'Source': 'Nicolas-Joseph Cugnot', 'Target': 'Steam-powered road vehicle', 'Relation Name': 'built'}, {'Source': 'François Isaac de Rivaz', 'Target': 'Internal combustion-powered automobile', 'Relation Name': 'designedAndConstructed'}, {'Source': 'Carl Benz', 'Target': 'Benz Patent-Motorwagen', 'Relation Name': 'invented'}, {'Source': 'Car', 'Target': '20th century', 'Relation Name': 'becameWidelyAvailableIn'}, {'Source': 'Model T', 'Target': 'Masses', 'Relation Name': 'affordableBy'}, {'Source': 'Model T', 'Target': 'Ford Motor Company', 'Relation Name': 'manufacturedBy'}, {'Source': 'Car', 'Target': 'US', 'Relation Name': 'rapidlyAdoptedIn'}, {'Source': 'Car', 'Target': 'Horse-drawn carriages', 'Relation Name': 'replaced'}, {'Source': 'Car', 'Target': 'World War II', 'Relation Name': 'demandIncreasedAfter'}, {'Source': 'Car', 'Target': 'Developed economy', 'Relation Name': 'isEssentialPartOf'}, {'Source': 'Car', 'Target': 'Controls', 'Relation Name': 'has'}, {'Source': 'Car', 'Target': 'Lamps', 'Relation Name': 'has'}, {'Source': 'Car', 'Target': 'Features and controls', 'Relation Name': 'addedTo'}, {'Source': 'Car', 'Target': 'Rear-reversing cameras', 'Relation Name': 'hasFeature'}, {'Source': 'Car', 'Target': 'Air conditioning', 'Relation Name': 'hasFeature'}, {'Source': 'Car', 'Target': 'Navigation systems', 'Relation Name': 'hasFeature'}, {'Source': 'Car', 'Target': 'In-car entertainment', 'Relation Name': 'hasFeature'}, {'Source': 'Car', 'Target': 'Internal combustion engine', 'Relation Name': 'isPropelledBy'}, {'Source': 'Car', 'Target': 'Fossil fuels', 'Relation Name': 'fueledBy'}, {'Source': 'Electric car', 'Target': 'Car', 'Relation Name': 'isA'}, {'Source': 'Electric car', 'Target': '2000s', 'Relation Name': 'becameCommerciallyAvailableIn'}, {'Source': 'Electric car', 'Target': 'Petrol-driven cars', 'Relation Name': 'predictedToCostLessThanBefore2025'}, {'Source': 'Car use', 'Target': 'Costs and benefits', 'Relation Name': 'has'}, {'Source': 'Individual', 'Target': 'Vehicle', 'Relation Name': 'acquires'}, {'Source': 'Individual', 'Target': 'Interest payments', 'Relation Name': 'pays'}, {'Source': 'Individual', 'Target': 'Repairs and maintenance', 'Relation Name': 'paysFor'}, {'Source': 'Individual', 'Target': 'Fuel', 'Relation Name': 'paysFor'}, {'Source': 'Individual', 'Target': 'Depreciation', 'Relation Name': 'experiences'}, {'Source': 'Individual', 'Target': 'Driving time', 'Relation Name': 'invests'}, {'Source': 'Individual', 'Target': 'Parking fees', 'Relation Name': 'paysFor'}, {'Source': 'Individual', 'Target': 'Taxes', 'Relation Name': 'pays'}, {'Source': 'Individual', 'Target': 'Insurance', 'Relation Name': 'paysFor'}, {'Source': 'Society', 'Target': 'Roads', 'Relation Name': 'maintains'}, {'Source': 'Society', 'Target': 'Land use', 'Relation Name': 'experiences'}, {'Source': 'Society', 'Target': 'Road congestion', 'Relation Name': 'experiences'}, {'Source': 'Society', 'Target': 'Air pollution', 'Relation Name': 'experiences'}, {'Source': 'Society', 'Target': 'Noise pollution', 'Relation Name': 'experiences'}, {'Source': 'Society', 'Target': 'Public health', 'Relation Name': 'affects'}, {'Source': 'Society', 'Target': 'Vehicle disposal', 'Relation Name': 'responsibleFor'}, {'Source': 'Traffic collisions', 'Target': 'Injury-related deaths', 'Relation Name': 'largestCauseOf'}, {'Source': 'Car use', 'Target': 'On-demand transportation', 'Relation Name': 'provides'}, {'Source': 'Car use', 'Target': 'Mobility', 'Relation Name': 'provides'}, {'Source': 'Car use', 'Target': 'Independence', 'Relation Name': 'provides'}, {'Source': 'Car use', 'Target': 'Convenience', 'Relation Name': 'provides'}, {'Source': 'Automotive industry', 'Target': 'Job and wealth creation', 'Relation Name': 'contributesTo'}, {'Source': 'Automotive industry', 'Target': 'Transportation provision', 'Relation Name': 'contributesTo'}]
    G = create_network(lst)
    options = {
    'node_color':"none",
    'node_size': 100,
    'node_shape':"s",
    'width': 3,
    'arrowstyle': '-|>',
    'arrowsize': 12,
    'arrows' : True
}
    nx.draw(G, with_labels=True, **options, bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))
    plt.show()