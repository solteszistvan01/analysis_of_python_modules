#Implement the get_module_from_the_name_of_the_module method and show it's usage!

from importlib import import_module

def get_module_from_the_name_of_the_module(the_name_of_the_module):
    try:
        module = import_module(the_name_of_the_module)
        return module
    except ModuleNotFoundError:
        print(f"Module {the_name_of_the_module} not found.")
        return None

# Usage example
numpy_module = get_module_from_the_name_of_the_module('numpy')
if numpy_module is not None:
    print(numpy_module.array([1, 2, 3]))  # Should print "[1 2 3]" if NumPy is installed

#Done

#Implement the get_classes_from_module method and show it's usage!

import inspect
def get_classes_from_module(module) -> list[type]:
    return [member for name, member in inspect.getmembers(module, inspect.isclass)]

# Usage example
module = get_module_from_the_name_of_the_module('pandas')  # Replace 'math' with the name of the module you are interested in
if module:
    classes = get_classes_from_module(module)
    for cls in classes:
        print(cls,type(cls))
#DONE

import sys
from pandas import DataFrame
import inspect
from types import FunctionType, MethodType

def NameAndDenotationAnalysis(Analysis):
  """
  Requirements:
  A Dependency graph must be created from the names and their corresponding denotations
  """
  def create_dependency_graph_from_the_names_and_their_corresponding_denotations():
    pass

  def __init__(self, the_names_and_their_corresponding_denotations):
    self.dependency_graph = create_dependency_graph_from_the_names_and_their_corresponding_denotations(the_names_and_their_corresponding_denotations)

class ClassAnalysis():
  the_callable_types = {"<class 'wrapper_descriptor'>", "<class 'builtin_function_or_method'>", "<class 'method_descriptor'>"}

  def __init__(self, the_class : type):
    self.class_to_be_analyzed = the_class

  def get_name_of_class_members_and_their_denotations(self) -> dict:
      attributes = {}
      for name in dir(the_class):
          try:
              value = getattr(the_class, name)
              attributes[name] = value
          except AttributeError:
              # Some special attributes/methods might raise an AttributeError
              continue
      return attributes
  def Function_or_Method(self, x) -> bool:
    if str(type(x)) in {"<class 'wrapper_descriptor'>", "<class 'builtin_function_or_method'>", "<class 'method_descriptor'>"}:
      return True
    else:
      return False
  def get_callable_objects_from_the_class_members(self) -> dict:
    the_callable_objects_from_the_class_members = dict()
    the_class_members = self.get_name_of_class_members_and_their_denotations()

    for x in the_class_members:
      if self.Function_or_Method(the_class_members[x]):
        the_callable_objects_from_the_class_members.update({x: the_class_members[x]})

    return the_callable_objects_from_the_class_members

  def get_non_callable_objects_from_the_class_members(self):
    the_non_callable_objects_from_the_class_members = dict()
    the_class_members = self.get_name_of_class_members_and_their_denotations()

    for x in the_class_members:
      if not self.Function_or_Method(the_class_members[x]):
        the_non_callable_objects_from_the_class_members.update({x: the_class_members[x]})

    return the_non_callable_objects_from_the_class_members

def ModuleAnalysis(Analysis):
  def __init__(self, the_analysis_of_the_classes, the_analysis_of_the_call_graphs, the_analysis_of_the_names_and_their_denotations, the_the_imported_modules):
    self.class_analyses = the_analysis_of_the_classes
    self.class_call_graph_analyses = the_analysis_of_the_call_graphs
    self.name_and_denotation_analyses = the_analysis_of_the_names_and_their_denotations
    self.imported_module_analyses = the_the_imported_modules
    pass

  def reveal_the_complexity_of_functions():
    pass

  def reveal_the_number_of_functions_defined_in_the_module():
    pass

  def reveal_the_call_graphs():
    pass

  def reveal_the_classes():
    pass

  def reveal_the_recursive_functions_used_in_the_module():
    pass

  def reveal_the_tree_of_the_modules_required_to_run_the_module():
    """
    The root is the top module and there is an edge between two modules, if one of them includes the other one.
    The leaves are the modules that don't inherit any other modules
    """
    pass

  def reveal_the_dependencies_of_the_variables_with_respect_to_other_variables():
    pass

  def reveal_the_size_of_the_denotations_of_names():
    pass

  def reveal_the_subobject_releationships_between_denotations_of_names():
    pass

  def reveal_the_undefined_functions():
    pass

  def reveal_the_number_of_functions_called_from_all_functions_defined():
    pass

  def reveal_the_depth_of_the_deepest_call_tree():
    pass

  def reveal_the_depth_of_the_shallowest_call_tree():
    pass

  def reveal_the_order_of_function_calls_for_all_functions_in_the_call_graph():
    pass

  def reveal_the_source_code_of_the_functions_used_in_the_module_in_order_of_dependency():
    pass

  def reveal_the_functions_and_their_arity() -> DataFrame:
    pass

  def reveal_the_classes_implementing_a_class(the_class):
    pass


#identifications
def identify_the_classes_and_their_subclasses_accessible_from_the_module_as_trees_together_with_the_methods_and_variables(the_module):
  """
  Input:
  The module
  Output:
  A collection of all classes defined in the module
  """

def identify_the_functions_defined_in_the_module_and_create_a_call_graph_of_the_functions(the_module):
  pass


def identify_the_names_in_the_module_denoting_python_objects(the_module):
  pass

def identify_the_imported_modules_of(the_module):
  pass


#creations
def create_the_call_graphs():
  """
  Output:
  A collection of call graphs from the function defined in the outmost scope of the module.
  """

#Analyses
def analyse_the_call_graphs(the_call_graphs):
  """
  Requirements:
  Be able to determine how is any function's parameters dependent on the input parameters to the root function for any call graph
  """

def analyse_the_classes(the_classes):
  pass

def analyse_the_names_and_their_denotations(the_names_and_their_denotations):
  pass

def analyse_the_imported_modules(the_imported_modules):
  pass

#Orderings
def reorder_the_methods_defined_in_a_class_according_to_the_order_of_calls(functions_defined_in_a_class):
  """
  Requirements:
  f < g if and only if f's definition is required to run g succesfully if and only if g is dependent on f.
  """
  pass

def analysis_of_the_module(the_module):
  the_classes = identify_the_classes_and_their_subclasses_accessible_from_the_module_as_trees_together_with_the_methods_and_variables(the_module)
  the_call_graphs = identify_the_functions_defined_in_the_module_and_create_a_call_graph_of_the_functions(the_module)
  the_names_and_their_denotations = identify_the_names_in_the_module_denoting_python_objects(the_module)
  the_imported_modules = identify_the_imported_modules_of(the_module)
  analysis_of_the_classes = analyse_the_classes(the_classes)
  analysis_of_the_call_graphs = analyse_the_call_graphs(the_call_graphs)
  analysis_of_the_names_and_their_denotations = analyse_the_names_and_their_denotations(the_names_and_their_denotations)
  analysis_of_the_imported_modules = analyse_the_imported_modules(the_imported_modules)

  return ModuleAnalysis(analysis_of_the_classes, analysis_of_the_call_graphs, analysis_of_the_names_and_their_denotations, analysis_of_the_imported_modules)

def functions_are_listed_in_order_of_dependency(the_list_of_functions) -> bool:
  pass


def main():
  the_name_of_the_module = sys.argv[1]
  the_module = get_module_from_the_name_of_the_module(the_name_of_the_module)
  return analysis_of_the_module(the_module)


def get_all_methods_of_the_class(the_class) -> dict:
    # Retrieve all methods, including static and class methods
    members = get_all_members_of_the_class(the_class)
    methods = {name : member for name, member in inspect.getmembers(the_class) if inspect.isfunction(member) or inspect.ismethod(member)}
    # Filter out methods not defined in this class
    #methods = [method for method in methods if method.__qualname__.startswith(the_class.__name__ + '.')]

    return methods

def get_all_members_of_the_class(the_class) -> dict:
    # Retrieve all methods, including static and class methods
    members = {name : member for name, member in inspect.getmembers(the_class)}

    return members
def get_all_method_names_of_class(cls):
    # Retrieve all methods, including static and class methods
    methods = [member for name, member in inspect.getmembers(cls) if inspect.isfunction(member) or inspect.ismethod(member)]

    # Filter out methods not defined in this class
    methods = [method for method in methods if method.__qualname__.startswith(cls.__name__ + '.')]

    # Get the names of the methods
    method_names = [method.__name__ for method in methods]

    return method_names


print(get_all_methods_of_the_class(list))

#Implement the get_classes_from_module method and show it's usage!

def get_name_of_class_members_and_their_denotations(cls) -> dict:
    attributes = {}
    for name in dir(cls):
        try:
            value = getattr(cls, name)
            attributes[name] = value
        except AttributeError:
            # Some special attributes/methods might raise an AttributeError
            continue
    return attributes

#Show the usage of the dir function in Python!

the_module = get_module_from_the_name_of_the_module('math')
the_classes = get_classes_from_module(the_module)
the_class = list

print("The type of dir(the_class) is",type(dir(the_class)))

the_list_of_names_to_objects_in_the_class = dir(the_class)
the_list_of_all_members_of_the_class = get_all_members_of_the_class(the_class)

print("It is", len(dir(the_class)) == len(the_list_of_all_members_of_the_class), "that the length of dir(the_class)","(",len(dir(the_class)),")", "is the same as the length of the list of all members of the class","(",len(the_list_of_all_members_of_the_class),")")

get_name_of_class_members_and_their_denotations(the_class)

for name in get_name_of_class_members_and_their_denotations(the_class):
  print("The name","\""+name+"\"","of type",type(name),"denotes",get_name_of_class_members_and_their_denotations(the_class)[name],"of type",type(get_name_of_class_members_and_their_denotations(the_class)[name]))

def identify_the_classes_and_their_subclasses_accessible_from_the_module_as_trees_together_with_the_methods_and_variables(the_module):
  """
  Input:
  The module
  Output:
  A collection of all classes defined in the module
  """
  the_list_of_classes_in_the_module = get_classes_from_module(the_module)

#An example of finding instance attributes in a class
import ast

def find_self_assignments(class_definition):
    attributes = set()
    tree = ast.parse(class_definition)
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for sub_node in ast.walk(node):
                if isinstance(sub_node, ast.Assign):
                    for target in sub_node.targets:
                        if isinstance(target, ast.Attribute):
                            if isinstance(target.value, ast.Name) and target.value.id == 'self':
                                attributes.add(target.attr)
    return attributes

# Example usage
class_definition = '''
class MyClass:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        self.strrrrr = lll

    def my_method(self):
        self.method_value = "something"
'''

attributes = find_self_assignments(class_definition)
print(attributes)

def determine_the_decision_complexity_of_a_function_by_showing_all_the_possible_propositional_models_that_might_occur_during_the_function_taking_the_names_of_the_boolean_variables_into_consideration_while_showing_the_possible_models():
  pass


def enumerate_all_the_properties_of_the_program_code_that_were_analysed_during_the_analysis():
  """
  Examples of similar enumerations: any glossary in a book.
  """
  pass

def non_static_analysis_of_functions(function):
  """
  the running of a function should be done in a similar manner as running of code is done with a compiler object with c++ code.
  """
  pass

def determine_the_running_time_of_a_function_after_the_possible_propositional_models_have_been_determined_for_the_function_with_random_parameters_that_have_nice_properties():
  pass

def static_analysis_of_functions():
  pass

def proofs_on_python_objects():
  pass

def for_a_collection_of_proofs_on_functions_written_by_some_panguage_capable_of_proving_statements_about_python_functions_prove_or_disprove_a_set_of_propositions_of_functions():
  pass
