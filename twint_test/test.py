import twint

# Configure
c = twint.Config()
c.Search = "scotus"
c.Limit = 20
c.Custom = 

# Run
twint.run.Search(c)