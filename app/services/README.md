API keys and specific requests for each service are typically handled within the service classes themselves. This is because these aspects are directly related to the service's main responsibility, which is interacting with a specific API.

However, if you find that your service classes are becoming too large or complex, or if there's a lot of shared logic between different service classes, it might make sense to delegate some tasks to helper classes or modules.

Here's a rough guideline:

API Keys: These are usually stored in environment variables for security reasons and loaded in the service class. If you have multiple keys or complex logic for loading keys, you might want to create a separate APIKeyManager class or module.

Creating Requests: This is typically handled in the service class, as each service might need to create requests in a different way. If there's shared logic between different services, you could create a RequestBuilder helper class or module.

Parsing Responses: If the logic for parsing responses is complex or shared between different services, you might want to create a ResponseParser helper class or module.

Error Handling: If your services need to handle many different types of errors, you might want to create a ErrorHandler helper class or module.

Remember, the goal is to keep your classes and modules small, focused, and easy to understand. If a class or module is becoming too large or complex, or if it's handling too many different tasks, it might be a good idea to split it up.