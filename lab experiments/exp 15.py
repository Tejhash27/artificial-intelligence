import math

class Node:
    """Represents a single decision node or leaf node in the tree."""
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature        # Index of the feature to split on
        self.threshold = threshold    # Threshold value for numerical splitting
        self.left = left              # Subtree for values below the threshold
        self.right = right            # Subtree for values above the threshold
        self.value = value            # Contains the predicted class classification if leaf node

    def is_leaf(self):
        return self.value is not None


class DecisionTreeClassifierScratch:
    def __init__(self, max_depth=10, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None

    def _gini_impurity(self, y):
        """Calculates the Gini Impurity of a label distribution dataset array."""
        m = len(y)
        if m == 0:
            return 0
        # Count occurrences of each unique label class classification
        counts = {}
        for item in y:
            counts[item] = counts.get(item, 0) + 1
        
        # Gini Formula: 1 - sum(p_i^2)
        gini = 1.0 - sum((count / m) ** 2 for count in counts.values())
        return gini

    def _split_data(self, X, y, feature, threshold):
        """Splits data indices based on an explicitly provided feature threshold index."""
        left_idx = [i for i, row in enumerate(X) if row[feature] <= threshold]
        right_idx = [i for i, row in enumerate(X) if row[feature] > threshold]
        return left_idx, right_idx

    def _best_split(self, X, y):
        """Finds the best feature index and value split criterion to maximize impurity drop."""
        best_gini_gain = -1
        split_idx, split_thresh = None, None
        
        n_samples, n_features = len(X), len(X[0])
        current_gini = self._gini_impurity(y)

        for feat in range(n_features):
            # Extract all column values for this specific feature index layout
            feature_values = [row[feat] for row in X]
            unique_thresholds = set(feature_values)
            
            for thresh in unique_thresholds:
                left_idx, right_idx = self._split_data(X, y, feat, thresh)
                if len(left_idx) == 0 or len(right_idx) == 0:
                    continue
                
                # Weighted average of children nodes impurity metrics
                n_l, n_r = len(left_idx), len(right_idx)
                y_l = [y[i] for i in left_idx]
                y_r = [y[i] for i in right_idx]
                
                child_gini = (n_l / n_samples) * self._gini_impurity(y_l) + (n_r / n_samples) * self._gini_impurity(y_r)
                gini_gain = current_gini - child_gini
                
                if gini_gain > best_gini_gain:
                    best_gini_gain = gini_gain
                    split_idx = feat
                    split_thresh = thresh

        return split_idx, split_thresh

    def _most_common_label(self, y):
        """Finds the most frequent label in an array sequence."""
        counts = {}
        for item in y:
            counts[item] = counts.get(item, 0) + 1
        return max(counts, key=counts.get) if counts else None

    def _build_tree(self, X, y, depth=0):
        n_samples = len(X)
        n_labels = len(set(y))

        # Check stopping criteria conditions
        if (depth >= self.max_depth or 
            n_labels == 1 or 
            n_samples < self.min_samples_split):
            leaf_value = self._most_common_label(y)
            return Node(value=leaf_value)

        # Find the optimal split conditions
        feat_idx, thresh = self._best_split(X, y)
        if feat_idx is None:
            return Node(value=self._most_common_label(y))

        # Recursively construct left and right child sub-trees
        left_idx, right_idx = self._split_data(X, y, feat_idx, thresh)
        
        left_child = self._build_tree([X[i] for i in left_idx], [y[i] for i in left_idx], depth + 1)
        right_child = self._build_tree([X[i] for i in right_idx], [y[i] for i in right_idx], depth + 1)
        
        return Node(feature=feat_idx, threshold=thresh, left=left_child, right=right_child)

    def fit(self, X, y):
        """Trains the Decision Tree model using the input dataset layout dimensions."""
        self.root = self._build_tree(X, y)

    def _predict_row(self, node, x):
        if node.is_leaf():
            return node.value
        
        if x[node.feature] <= node.threshold:
            return self._predict_row(node.left, x)
        return self._predict_row(node.right, x)

    def predict(self, X):
        """Predicts classifications for an input matrix dataset array configuration."""
        return [self._predict_row(self.root, row) for row in X]


# --- Execution Flow ---
if __name__ == "__main__":
    print("=" * 60)
    print("        CUSTOM DECISION TREE CLASSIFIER (FROM SCRATCH)")
    print("=" * 60)

    # Sample Dataset: [Age, Income Level (High=1, Low=0)]
    # Target label: Will Buy Product? (Yes=1, No=0)
    X_train = [
        [25, 1], [35, 1], [45, 0], [20, 0], [55, 1], [60, 0], [22, 1], [40, 1]
    ]
    y_train = [0, 1, 1, 0, 1, 0, 0, 1]

    # Initialize and fit the custom tree classifier
    clf = DecisionTreeClassifierScratch(max_depth=3)
    clf.fit(X_train, y_train)

    # Test predictions against new incoming samples
    X_test = [
        [30, 1],  # Expected: Likely 1 (Mid-age, High Income)
        [50, 0]   # Expected: Likely 0 or 1 depending on tree threshold evaluations
    ]
    
    predictions = clf.predict(X_test)
    
    print("Training Configuration Evaluation Completed.")
    print("-" * 60)
    for i, test_sample in enumerate(X_test):
        print(f"Input Features: Age={test_sample[0]}, Income Code={test_sample[1]} -> Predicted Label output: {predictions[i]}")
    print("=" * 60)
