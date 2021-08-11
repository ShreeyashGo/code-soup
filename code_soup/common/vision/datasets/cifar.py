from typing import Any, Tuple

import torchvision.datasets as datasets
from torch.utils.data import Dataset
from torchvision import transforms


class CIFARDataset(Dataset):
    """
    `CIFAR <https://www.cs.toronto.edu/~kriz/cifar.html>`_ Dataset. Built using TorchVision Dataset class.
    Args:
        transform (callable, optional): A function/transform that  takes in an PIL image
            and returns a transformed version. E.g, ``transforms.RandomCrop``
    """

    def __init__(self, transform: callable = None):
        """
        Parameters
        ----------
        transform : torchvision.transforms
            - A transform to be applied on the dataset
        """

        self.train_data = datasets.CIFAR10(
            root="./input/data", train=True, download=True, transform=transform
        )

    def __len__(self) -> int:
        """
        Returns
        -------
        length : int
            - Length of the dataset
        """
        return len(self.train_data)

    def __getitem__(self, idx: int) -> Tuple[Any, Any]:
        """
        Returns
        -------
        element : torch.Tensor
            - A element from the dataset
        """
        return self.train_data.__getitem__(idx)


if __name__ == "__main__":
    CIFARDataset(transform=transforms.Compose([transforms.ToTensor()]))