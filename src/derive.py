import torch

import utility
import data
import model
import loss
from option import args
from trainer import Trainer
from controller_trainer import Controller_Trainer

torch.manual_seed(args.seed)
checkpoint = utility.checkpoint(args)

def main():
    global model
    global loss
    if args.data_test == 'video':
        from videotester import VideoTester
        model = model.Model(args, checkpoint)
        t = VideoTester(args, model, checkpoint)
        t.test()
    else:
        if checkpoint.ok:
            loader = data.Data(args)
            share_model = model.Model(args, checkpoint)
            loss = loss.Loss(args, checkpoint) if not args.test_only else None
            t = Trainer(args, loader, share_model, loss, checkpoint)
            t.derive()
            checkpoint.done()

if __name__ == '__main__':
    main()
