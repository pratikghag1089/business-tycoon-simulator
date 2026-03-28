# Business Tycoon Simulator (MVP) - Technical Architecture

## Tech Stack
- **Language**: Python 3.10+ with Pygame for rendering and game loop management
- **Justification**: Python enables rapid development of complex simulation logic while Pygame provides lightweight 2D rendering suitable for a business simulation UI. The language's rich ecosystem supports the mathematical modeling required for economic simulation without excessive overhead.

## Component Design

### Game Engine (`engine.py`)
- **Responsibility**: Manages game loop, timing, state transitions, and coordinates all systems
- **Key Class**: `GameEngine` with methods `run()`, `update(delta_time)`, `render()`, `handle_input()`
- **Connections**: Initializes and coordinates World, UI, and AI systems

### World Model (`world.py`)
- **Responsibility**: Contains all game entities (towns, companies, factories, stores) and manages spatial relationships
- **Key Classes**: `World`, `Town`, `Connection`
- **Key Functions**: `World.update(delta_time)`, `World.get_towns()`, `Town.get_stores()`
- **Connections**: Contains all Company instances and provides market data to other systems

### Economic Simulation (`economy.py`)
- **Responsibility**: Handles market dynamics, pricing, demand calculation, and financial transactions
- **Key Classes**: `Market`, `FinancialSystem`
- **Key Functions**: `Market.calculate_demand(product, town)`, `FinancialSystem.process_transactions()`
- **Connections**: Receives production data from Companies, provides demand data to Stores and AI

### Company Management (`company.py`)
- **Responsibility**: Represents player and AI companies with financials, production, and inventory
- **Key Classes**: `Company`, `Factory`, `Store`, `Product`
- **Key Functions**: `Company.produce(product, quantity)`, `Company.get_net_worth()`, `Factory.produce_batch()`
- **Connections**: Contains Factory and Store instances, interacts with Economy for pricing

### AI System (`ai.py`)
- **Responsibility**: Controls competitor companies with strategic decision-making
- **Key Class**: `AIController` with method `make_decisions(company, world_state)`
- **Connections**: Reads World state, issues commands to Company instances

### UI System (`ui.py`)
- **Responsibility**: Renders game state and handles player input through Pygame
- **Key Classes**: `UIManager`, `DashboardScreen`, `ProductionScreen`
- **Key Functions**: `UIManager.render()`, `UIManager.handle_click()`
- **Connections**: Reads Company and World data for display, sends player commands to Game Engine

## Data Flow
1. **Input**: Player actions via UI → Game Engine processes commands
2. **Update**: Game Engine → updates World (time progression) → updates all Companies
3. **Economic Cycle**: Companies produce goods → Market calculates demand → Stores sell goods → Financial system processes revenue
4. **AI Decisions**: AI Controller analyzes World state → issues strategic commands to AI Companies
5. **Output**: World state → UI renders current game state to player

## Key Design Decisions
- **Turn-based with real-time elements**: Economic cycles occur at fixed intervals (monthly) while allowing continuous player interaction
- **Simplified logistics**: Goods teleport between connected towns with time delays rather than physical transportation simulation
- **Component-based entities**: Companies, Factories, and Stores are separate objects for flexible composition
- **Deterministic simulation**: All random elements use seeded RNG for reproducible game states and debugging

json
[
  {"path": "main.py", "description": "Entry point: initializes Pygame, creates GameEngine instance, and starts the game loop"},
  {"path": "engine.py", "description": "Game engine: manages the main loop, timing, state transitions, and coordinates World, UI, and AI systems via update/render/handle_input cycle"},
  {"path": "world.py", "description": "World model: contains Town, Connection classes and manages all game entities (companies, factories, stores) with spatial relationships between 4-5 towns"},
  {"path": "economy.py", "description": "Economic simulation: Market class calculates demand per town based on product attributes/price/brand, FinancialSystem handles transactions, loans, and net worth tracking"},
  {"path": "company.py", "description": "Company management: Company class with cash/debt/inventory, Factory for production consuming raw materials, Store for retail sales, Product with category/quality/features attributes"},
  {"path": "ai.py", "description": "AI system: AIController class manages 10-20 autonomous competitor companies making decisions on production, pricing, expansion, and supply chain management each game tick"},
  {"path": "ui.py", "description": "UI rendering: Pygame-based interface with financial dashboard, product design screen, factory/store management panels, map view, and inventory displays"},
  {"path": "config.py", "description": "Game configuration: constants for starting cash, loan limits, victory thresholds, town definitions, product categories, raw material types, and simulation tuning parameters"}
]
```