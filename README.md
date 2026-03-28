# Business Tycoon Simulator

A single-player, Windows desktop business simulation game where players build and manage a corporate empire to achieve financial dominance through deep economic strategy, targeting hardcore fans of classic tycoon games.

## Goals

- Provide a complex, purely financial simulation focused on market competition and wealth accumulation.
- Deliver a scalable game world with multiple towns and AI competitors to ensure strategic depth and replayability.
- Recreate the engaging economic management depth of classics like Capitalism II for a modern audience.

---
## Architecture

- **Language**: Python 3.10+ with Pygame for rendering and game loop management
- **Justification**: Python enables rapid development of complex simulation logic while Pygame provides lightweight 2D rendering suitable for a business simulation UI. The language's rich ecosystem supports the mathematical modeling required for economic simulation without excessive overhead.

### Project Files

- `main.py` — Entry point: initializes Pygame, creates GameEngine instance, and starts the game loop
- `engine.py` — Game engine: manages the main loop, timing, state transitions, and coordinates World, UI, and AI systems via update/render/handle_input cycle
- `world.py` — World model: contains Town, Connection classes and manages all game entities (companies, factories, stores) with spatial relationships between 4-5 towns
- `economy.py` — Economic simulation: Market class calculates demand per town based on product attributes/price/brand, FinancialSystem handles transactions, loans, and net worth tracking
- `company.py` — Company management: Company class with cash/debt/inventory, Factory for production consuming raw materials, Store for retail sales, Product with category/quality/features attributes
- `ai.py` — AI system: AIController class manages 10-20 autonomous competitor companies making decisions on production, pricing, expansion, and supply chain management each game tick
- `ui.py` — UI rendering: Pygame-based interface with financial dashboard, product design screen, factory/store management panels, map view, and inventory displays
- `config.py` — Game configuration: constants for starting cash, loan limits, victory thresholds, town definitions, product categories, raw material types, and simulation tuning parameters

_See `architecture.md` for the full design._

---

_Development log will be appended as issues are completed._

## Development Log

### Cycle 1 — #1: Set up core game engine and world model

**APPROVE** — The implementation fully meets all acceptance criteria. The game window opens and runs at stable 60 FPS, game time advances and is displayed in the window title, the world contains 5 distinct towns with different populations, and configuration constants are properly accessible from other modules. No critical bugs were found.
