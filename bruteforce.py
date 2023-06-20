def calculate_total_cost(warehouse_file):
    # Veri dosyasını okuyalım
    with open(warehouse_file, 'r') as file:
        lines = file.readlines()

    depot_count, customer_count = map(int, lines[0].split())

    depots = []
    for line in lines[1:depot_count + 1]:
        capacity, setup_cost = map(float, line.split())
        depots.append((capacity, setup_cost))

    customer_demands = []
    customer_costs = []
    for i in range(customer_count):
        demand = int(lines[depot_count + 1 + i * 2])
        customer_demands.append(demand)
        costs = list(map(float, lines[depot_count + 2 + i * 2].split()))
        customer_costs.append(costs)

    # Müşteriye atanan depoları bulalım
    assigned_depots = []
    for i in range(customer_count):
        min_cost = float('inf')
        assigned_depot = None
        for j in range(depot_count):
            cost = customer_costs[i][j]
            if cost < min_cost:
                min_cost = cost
                assigned_depot = j
        assigned_depots.append(assigned_depot)

    # Toplam maliyeti hesaplayalım
    total_cost = 0
    for i in range(customer_count):
        assigned_depot = assigned_depots[i]
        total_cost += depots[assigned_depot][1]

    return total_cost, assigned_depots

# Veri dosyasını burada belirtiyoruz
warehouse_file = 'wl_16_1.txt'

# Toplam maliyeti ve müşteriye atanan depoları hesaplıyoruz
total_cost, assigned_depots = calculate_total_cost(warehouse_file)

# Sonuçları yazdıralım
print("Toplam maliyet:", total_cost)
print("Müşteriye atanan depolar:", " ".join(str(dep) for dep in assigned_depots))


