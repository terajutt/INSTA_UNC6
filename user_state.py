"""
User state management for the bot.
"""

import time
from typing import Dict, Any, Optional

class UserStateManager:
    """Manage user states and game states."""
    
    def __init__(self):
        self.user_states = {}
        self.game_states = {}
        self.user_locations = {}
        
    def initialize_user(self, user_id: int):
        """Initialize user state."""
        self.user_states[user_id] = {
            'initialized': True,
            'first_seen': time.time(),
            'last_active': time.time()
        }
        
    def update_user_location(self, user_id: int, location: str):
        """Update user's current location in the bot."""
        self.user_locations[user_id] = location
        if user_id in self.user_states:
            self.user_states[user_id]['last_active'] = time.time()
            
    def get_user_location(self, user_id: int) -> str:
        """Get user's current location."""
        return self.user_locations.get(user_id, "main_menu")
        
    def set_game_state(self, user_id: int, game_state: Dict[str, Any]):
        """Set game state for user."""
        self.game_states[user_id] = game_state
        
    def get_game_state(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Get game state for user."""
        return self.game_states.get(user_id)
        
    def clear_game_state(self, user_id: int):
        """Clear game state for user."""
        if user_id in self.game_states:
            del self.game_states[user_id]