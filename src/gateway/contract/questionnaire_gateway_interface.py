from abc import ABC, abstractmethod


class QuestionnaireGatewayInterface(ABC):
    
    @abstractmethod    
    async def get_async(self):
        """get questionnaires async"""
        
        raise NotImplementedError("Method not implemented")
