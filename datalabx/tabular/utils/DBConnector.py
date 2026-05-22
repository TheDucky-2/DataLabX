import duckdb
from typing import Literal, Optional

class DuckDBConnector:

    def __init__(self, conn_type: Literal["memory", "persistent"]="memory", file_name:Optional[str]=None):
        if conn_type == "memory":
            self.conn = duckdb.connect()
        elif conn_type == "persistent" and file_name is not None:
            self.conn = duckdb.connect(file_name)
    
    def query(self, query:str, to_df:bool=False):
    
        result = self.conn.sql(query)

        if to_df:
            return result.to_df()
        
        return result

    def close(self):
        self.conn.close()