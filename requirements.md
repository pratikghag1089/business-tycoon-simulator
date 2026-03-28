# Requirements: Business Tycoon Simulator (MVP)

## Project Summary
A single-player, Windows desktop business simulation game where players build and manage a corporate empire to achieve financial dominance through deep economic strategy, targeting hardcore fans of classic tycoon games.

## Goals
- Provide a complex, purely financial simulation focused on market competition and wealth accumulation.
- Deliver a scalable game world with multiple towns and AI competitors to ensure strategic depth and replayability.
- Recreate the engaging economic management depth of classics like Capitalism II for a modern audience.

## Scope

### In Scope
1.  **Core Company Management:** Founding a company, managing finances (cash, loans, stock), and setting basic operational parameters.
2.  **Product Creation & Production:** Designing products with defined attributes, establishing factories, and setting production quantities.
3.  **Supply Chain Simulation:** Sourcing raw materials, managing inventory, and distributing finished goods to retail outlets.
4.  **Market & Competition:** A dynamic market with consumer demand, pricing, brand image, and AI-controlled competitor entities.
5.  **Game World & Entities:** A map containing 4-5 distinct towns and 10-20 AI-controlled competing companies.
6.  **Financial Victory Condition:** A clear win state based on achieving a target net worth or market share dominance.

### Deferred
- Political systems, lobbying, or government interaction.
- Real estate investment and property management.
- Multiplayer or online features.
- Advanced UI/UX features like detailed graphs or scenario editors.
- Sound design and complex visual animations.

## User Stories
1.  As a player, I want to found and name my own company so that I can begin building my business empire.
2.  As a player, I want to design and manufacture products so that I can generate revenue and compete in the market.
3.  As a player, I want to manage my supply chain from raw materials to retail so that I can optimize costs and meet demand.
4.  As a player, I want to compete against multiple AI-controlled companies so that the game world feels challenging and dynamic.
5.  As a player, I want to track my company's financial performance and net worth so that I can measure my progress toward becoming the richest entity.

## Acceptance Criteria
1.  **Company Management:**
    *   Player can name their company and choose a starting town.
    *   Player can view a financial dashboard showing cash, debt, revenue, expenses, and net worth.
    *   Player can take out and repay loans.
2.  **Product & Production:**
    *   Player can create a product by selecting a category and defining attributes (e.g., quality, features).
    *   Player can build a factory, assign it to produce a specific product, and set a production quantity.
    *   Production consumes required raw materials from inventory.
3.  **Supply Chain:**
    *   Player can establish contracts to purchase raw materials, which are delivered to a warehouse.
    *   Player can ship finished goods from factories to owned or third-party retail stores in various towns.
    *   Inventory levels for raw materials and finished goods are tracked and visible.
4.  **Market & AI:**
    *   The game simulates consumer demand in each town based on product attributes, price, and brand image.
    *   AI competitors operate autonomously, producing goods, setting prices, and expanding their businesses.
    *   Player actions (pricing, marketing) affect their market share and brand image.
5.  **Game World & Victory:**
    *   The game map contains at least 4 distinct towns with independent market conditions.
    *   At least 10 AI-controlled competitor entities exist at game start.
    *   The game declares a victory when the player's net worth is the highest and exceeds a predefined threshold.